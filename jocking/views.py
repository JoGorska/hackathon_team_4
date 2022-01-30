from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Jocke
from .forms import JockeForm


class JockesList(generic.ListView):
    '''
    class view enabling to display the list of jockes with pagination
    '''
    model = Jocke
    queryset = Jocke.objects.order_by('-created_on')
    template_name = 'jockes_list_paginated.html'
    paginate_by = 6


class AddNewJocke(CreateView):
    '''
    class view in get - gets the jocke_form and in post - posts the form
    and creates new jocke
    '''
    template_name = 'jocke_form.html'
    form_class = JockeForm
    success_url = 'jockes_list'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'jocke_form.html',
            {
                'jocke_form': JockeForm()
            },
        )

    def post(self, request, *args, **kwargs):

        jocke_form = JockeForm(data=request.POST)
        if jocke_form.is_valid():
            jocke_form.instance.author_id = request.user.id

            jocke = jocke_form.save(commit=False)
            jocke.save()

        else:
            jocke_form = JockeForm()

        return redirect('jockes_list')


class JockeEyes(View):
    '''
    adds user to the users list that have clicked the eye
    '''
    def post(self, request, jocke_id):
        jocke = get_object_or_404(Jocke, id=jocke_id)
        if jocke.eyes.filter(id=request.user.id).exists():
            jocke.eyes.remove(request.user)
        else:
            jocke.eyes.add(request.user)

        return redirect('jockes_list')
