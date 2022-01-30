""" Forms for Wellbeing app """
# pylint: disable=too-few-public-methods
from django import forms
from .models import Mood


class MoodForm(forms.ModelForm):
    '''
    form to create new traffic alerts
    '''
    class Meta:
        """ meta for MoodForm class """
        model = Mood
        # important - don't forget comma at the end of the list of fields
        fields = ('mood', )
