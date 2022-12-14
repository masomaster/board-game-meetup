from types import MethodType
from django.shortcuts import redirect, render 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Meeting, Photo, MeetingPhoto
from main_app.forms import MeetingForm
import uuid
import boto3
import os

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def games_index(request):
  games = Game.objects.filter(user=request.user)
  return render(request, 'games/games_index.html', {'games': games})

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  meeting_form = MeetingForm()
  return render(request, 'games/games_detail.html', {'game': game, 'form': meeting_form})

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = [
    'name', 'min_player', 'max_player', 'avg_game_play', 'difficulty_rating', 'genre', 'min_age', 'description', 'notes'
  ]

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = [
    'name', 'min_player', 'max_player', 'avg_game_play', 'difficulty_rating', 'genre', 'min_age', 'description'
  ]

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

class MeetingDetail(LoginRequiredMixin, DetailView):
  model = Meeting

  def get_context_data(self, **kwargs):
    context = super(MeetingDetail, self).get_context_data(**kwargs)
    meeting = self.get_object()
    players = meeting.players.all()
    context['players'] = players
    return context

class MeetingUpdate(LoginRequiredMixin, UpdateView):
  model = Meeting
  fields = ['name', 'date', 'location', 'min_ppl', 'max_ppl']

class MeetingDelete(LoginRequiredMixin, DeleteView):
  model = Meeting
  success_url = '/meetings/'

@login_required
def create_meeting(request, game_id):
  form = MeetingForm(request.POST)
  new_meeting = 0
  if form.is_valid():
    new_meeting = form.save(commit=False)
    new_meeting.game_id = game_id
    new_meeting.organizer_id = request.user.id
    new_meeting.save()
    new_meeting.players.add(request.user)
  return redirect('meetings_detail', 
    pk = new_meeting.id)

@login_required
def join_meeting(request, meeting_id):
  Meeting.objects.get(id=meeting_id).players.add(request.user.id)
  return redirect('meetings_index')

def meetings_list(request):
  my_meetings = Meeting.objects.filter(organizer=request.user)
  non_joined_meetings = Meeting.objects.exclude(players__id=request.user.id)
  joined_meetings = Meeting.objects.filter(players__id=request.user.id)  
  return render (request, 'meetings/meetings_index.html', {
    'my_meetings': my_meetings,
    'non_joined_meetings': non_joined_meetings,
    'joined_meetings': joined_meetings,
  })

@login_required
def leave_meeting(request, meeting_id):
    meeting = Meeting.objects.get(id=meeting_id)
    meeting.players.remove(request.user.id)
    return redirect('meetings_index')

@login_required
def add_photo(request, game_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, game_id=game_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('games_detail', game_id=game_id)

@login_required
def add_meeting_photo(request, meeting_id):
    meeting_photo_file = request.FILES.get('meeting_photo-file', None)
    if meeting_photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + meeting_photo_file.name[meeting_photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(meeting_photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            MeetingPhoto.objects.create(url=url, meeting_id=meeting_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('meetings_detail', pk=meeting_id)