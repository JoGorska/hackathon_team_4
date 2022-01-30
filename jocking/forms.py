""" Forms for joking app """
# pylint: disable=too-few-public-methods
from django import forms
from .models import Jocke


class JockeForm(forms.ModelForm):
    '''
    form to create new traffic alerts
    '''
    class Meta:
        """ meta data for JockeForm class """
        model = Jocke
        # important - don't forget coma at the end of the list of fields
        fields = ('headline', 'punchline', )
