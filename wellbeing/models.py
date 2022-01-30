""" Models for wellbeing app """
# pylint: disable=too-few-public-methods
from django.db import models
from django.contrib.auth.models import User

MOOD_CHOICES = [
    ('tired', 'Tired'),
    ('bored', 'Bored'),
    ('stressed', 'Stressed'),
    ('unknown', 'Unknown'),
    ('happy', 'Happy'),
    ('anxious', 'Anxious'),
    ('sad', 'Sad')
]


class Mood(models.Model):
    '''
    Model that takes the data about the mood from the user
    '''
    created_on = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="mood")
    mood = models.CharField(max_length=200, choices=MOOD_CHOICES,)


    class Meta:
        """ Meta data for Mood class """
        ordering = ['-created_on']


    def __str__(self):
        """ string method for Mood class """
        return f'Mood on {self.created_on} is {self.mood}'
