from django.forms import ModelForm
from .models import Meeting

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['name', 'date', 'location', 'min_ppl', 'max_ppl']