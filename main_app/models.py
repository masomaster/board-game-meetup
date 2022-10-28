from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game (models.Model):
    name = models.CharField(max_length=50)
    min_player = models.IntegerField()
    max_player = models.IntegerField(null=True)
    avg_game_play = models.IntegerField()
    difficulty_rating = models.IntegerField(null=True)
    genre = models.CharField(max_length=50, null=True)
    min_age = models.IntegerField(default=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.name