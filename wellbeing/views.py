from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Mood
from .forms import MoodForm


class HomeView(CreateView):
    '''
    
    '''
    template_name = 'templates/index.html'
    form_class = MoodForm
    def get(self, request, *args, **kwargs):

        context = {
            'mood_form': MoodForm,
        }
        return render(request, 'index.html', context)
    def post(self, request, *args, **kwargs):
        form = MoodForm()


class PostMood(CreateView):
    '''
    
    '''

    def post(self, request, *args, **kwargs):
        mood_form = MoodForm(data=request.POST)
        if mood_form.is_valid():
            mood_form.instance.author = request.user.id
            mood_instance = mood_form.save(comit=False)
            mood_instance.save()
        else:
            mood_form = MoodForm()
        return HttpResponseRedirect('/')
