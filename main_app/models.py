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
    # meetings = models.ManyToManyField(Meeting)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, blank= True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'game_id': self.id})

class Meeting(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Meeting Date') # do we want to set a default date?
    location = models.CharField(max_length=100)
    min_ppl = models.IntegerField()
    max_ppl = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null = True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_created", null = True) # in form, automatically assign creator to this field
    players = models.ManyToManyField(User, related_name="user_playing", null = True) # on form, automatically assign creator to this join table AND allow other users to click a "join" button that will add them to this join table

    def __str__(self):
        return f"{self.name} on {self.date}"

    def get_absolute_url(self):
        return reverse('meetings_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']