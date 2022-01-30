from django.contrib import admin
from .models import Jocke


@admin.register(Jocke)
class JockeAdmin(admin.ModelAdmin):
    '''
    class enabling admin see the model with details and search fields
    '''
    list_display = ('id', 'headline', 'author')
    search_fields = ['headline', 'author']
    list_filter = ('author', 'created_on')
