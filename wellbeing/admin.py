""" admin settings for wellbeing app """
from django.contrib import admin
from .models import Mood


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    '''
    class enabling admin see the Mood model
    '''
    list_display = ('created_on', 'author', 'mood')
    search_fields = ['author', 'mood']
    list_filter = ('author', 'created_on')
