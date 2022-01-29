from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
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
    template_name = 'index.html'
    form_class = MoodForm
    success_url = 'home'

    def post(self, request, author_id, *args, **kwargs):
        mood_form = MoodForm(data=request.POST)

        if mood_form.is_valid():
            author = get_object_or_404(User, id=author_id)
            mood_form.instance.author = author
            mood_instance = mood_form.save()
        else:
            mood_form = MoodForm()
        return HttpResponseRedirect("/")


class ClickMood(CreateView):
    '''
    saves object mood into database and redirects user to page 
    corresponding with his mood
    '''
    form_class = MoodForm
    template_name = 'index.html'
    def get(self, request, author_id, mood, *args, **kwargs):
        author = get_object_or_404(User, id=author_id)
        mood_object = Mood.objects.create(author=author, mood=mood)
        mood_object.save()
        if mood_object.mood == 'tired':
            return render(request, 'tired.html')
        elif mood_object.mood == 'bored':
            return render(request, 'bored.html')
        elif mood_object.mood == 'happy':
            return render(request, 'happy.html')
        elif mood_object.mood == 'stressed':
            return render(request, 'stressed.html')
        else:
            return HttpResponseRedirect("/")

