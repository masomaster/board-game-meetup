from django.contrib import admin
from .models import Game, Meeting, Photo, MeetingPhoto

# Register your models here.
admin.site.register(Game)
admin.site.register(Meeting)
admin.site.register(Photo)
admin.site.register(MeetingPhoto)