from django import forms
from .models import Jocke


class JockeForm(forms.ModelForm):
    '''
    form to create new traffic alerts
    '''
    class Meta:
        model = Jocke
        # important - don't forget coma at the end of the list of fields
        fields = ('headline', 'punchline', )
