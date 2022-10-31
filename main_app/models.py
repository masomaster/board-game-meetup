from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Game (models.Model):
    name = models.CharField(max_length=50)
    min_player = models.IntegerField()
    max_player = models.IntegerField(blank= True, null=True)
    avg_game_play = models.IntegerField()
    difficulty_rating = models.IntegerField(blank= True, null=True)
    genre = models.CharField(max_length=50, blank= True)
    min_age = models.IntegerField(default=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, blank= True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'game_id': self.id})