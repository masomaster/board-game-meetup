from types import MethodType
from django.shortcuts import redirect, render 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from main_app.forms import MeetingForm

from .models import Game, Meeting

# Create your views here.
def home(request):
  return render(request, 'home.html')

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
    'name', 'min_player', 'max_player', 'avg_game_play', 'difficulty_rating', 'genre', 'min_age', 'description'
  ]

  def form_valid(self, form):
    print('this got to view function')
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

class MeetingList(LoginRequiredMixin, ListView):
  model = Meeting
  fields = ['name', 'date', 'location', 'min_ppl', 'max_ppl']

class MeetingDetail(LoginRequiredMixin, DetailView):
  model = Meeting

class MeetingCreate(LoginRequiredMixin, CreateView):
  model = Meeting
  fields = ['name', 'date', 'location', 'min_ppl', 'max_ppl']

class MeetingUpdate(LoginRequiredMixin, UpdateView):
  model = Meeting
  fields = ['name', 'date', 'location', 'min_ppl', 'max_ppl']

class MeetingDelete(LoginRequiredMixin, DeleteView):
  model = Meeting
  success_url = '/meetings/'

@login_required
def create_meeting(request, game_id):
  form = MeetingForm(request.POST)
  if form.is_valid():
    new_meeting = form.save(commit=False)
    new_meeting.game_id = game_id
    new_meeting.organizer_id = request.user.id
    new_meeting.save()
  return redirect('meetings_index') # send to detail page if this works