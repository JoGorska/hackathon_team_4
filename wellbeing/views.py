""" Views for wellbeing app """
# pylint: disable=too-many-ancestors
# pylint: disable=arguments-differ
# pylint: disable=no-member
# pylint: disable=unused-variable
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Mood
from .forms import MoodForm


class HomeView(CreateView):
    '''
    View to render home page
    '''
    template_name = 'templates/index.html'
    form_class = MoodForm

    def get(self, request, *args, **kwargs):

        context = {
            'mood_form': MoodForm,
        }
        return render(request, 'index.html', context)


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
        if mood_object.mood == 'bored':
            return render(request, 'bored.html')
        if mood_object.mood == 'happy':
            return render(request, 'happy.html')
        if mood_object.mood == 'stressed':
            return render(request, 'stressed.html')

        return HttpResponseRedirect("/")


def get_tired_page(request):
    """ View to return tired page """

    return render(request, 'tired.html')


def get_bored_page(request):
    """ View to return bored page """

    return render(request, 'bored.html')


def get_happy_page(request):
    """ View to return happy page """

    return render(request, 'happy.html')


def get_stressed_page(request):
    """ View to return stressed page """

    return render(request, 'stressed.html')
