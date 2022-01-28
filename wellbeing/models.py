from django.db import models
from django.contrib.auth.models import User

MOOD_CHOICES = [
    ('unknown', 'Unknown'),
    ('happy', 'Happy'),
    ('anxious', 'Anxious'),
    ('sad', 'Sad')
]

class Mood(models.Model):
    '''
    Model that takes the data about the mood from the user
    '''
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="mood")
    mood = models.CharField(max_length=200, choices=MOOD_CHOICES,
                              default='unknown')

class Meta:
        ordering = ['-created_on']

def __str__(self):
    return(f'Mood on {self.created_on} is {self.mood}')