from django.db import models

# Create your models here.
class Game (models.Model):
    name = models.CharField(max_length=50)
    min_player = models.IntegerField()
    max_player = models.IntegerField()
    avg_game_play = models.IntegerField()
    difficulty_rating = models.IntegerField()
    genre = models.CharField(max_length=50)
    min_age = models.IntegerField(default=5)

    def __str__(self):
        return self.name

