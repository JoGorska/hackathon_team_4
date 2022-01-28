
from .models import Mood
from django import forms


class MoodForm(forms.ModelForm):
    '''
    form to create new traffic alerts
    '''
    class Meta:
        model = Mood
        # important - don't forget coma at the end of the list of fields
        fields = ('mood', )