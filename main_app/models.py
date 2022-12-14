from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Game (models.Model):
    name = models.CharField(max_length=50)
    min_player = models.IntegerField('Minimum # Players')
    max_player = models.IntegerField('Maximum # Players', blank=True, null=True)
    avg_game_play = models.IntegerField()
    difficulty_rating = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True)
    min_age = models.IntegerField(default=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, blank=True)
    notes = models.TextField('Private notes (e.g., strategy, etc.)', max_length=250, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'game_id': self.id})

class Meeting(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Meeting Date')
    location = models.CharField(max_length=100)
    min_ppl = models.IntegerField('Minimum # of players')
    max_ppl = models.IntegerField('Maximum # of players')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_created", null=True)
    players = models.ManyToManyField(User, related_name="user_playing")

    def __str__(self):
        return f"{self.name} on {self.date}"

    def get_absolute_url(self):
        return reverse('meetings_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"

class MeetingPhoto(models.Model):
    url = models.CharField(max_length=200)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for meeting_id: {self.meeting_id} @{self.url}"