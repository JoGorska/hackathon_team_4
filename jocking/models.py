from django.db import models
from django.contrib.auth.models import User

class Jocke(models.Model):
    '''
    Jocke model to record jockes posted by the users
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="jocke")
    created_on = models.DateTimeField(auto_now=True)
    headline = models.TextField()
    punchline = models.TextField()
    eyes = models.ManyToManyField(User, related_name='thanks', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return (f"Headilne {self.headline} by {self.author}")

    def number_of_eyes(self):
        return self.eyes.count()
