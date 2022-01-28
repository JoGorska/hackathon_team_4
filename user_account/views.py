from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import UserForm


class RegisterUserView(CreateView):
    """
    class view to register user as a build in User model from django
    """

    template_name = "users/register.html"
    form_class = UserForm
    success_url = reverse_lazy("/")

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
    form_class = User
    success_url = 'home'