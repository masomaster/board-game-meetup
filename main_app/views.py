from django.shortcuts import redirect, render 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView

from .models import Game

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