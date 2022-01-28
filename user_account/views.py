from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UserForm


class RegisterUserView(CreateView):
    """
    class view to register user as a build in User model from django
    """

    template_name = "registration/register.html"
    form_class = UserForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        new_user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, new_user)
        return HttpResponseRedirect(self.success_url)


class HomeView(CreateView):
    '''

    '''
    template_name = 'index.html'
    model = User
    form = UserForm
    success_url = 'home'