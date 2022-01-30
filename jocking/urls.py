from django.urls import path
from . import views

urlpatterns = [
    path('', JockesList.as_view(), name='jockes_list'),
    path('add_jocke', views.AddNewJocke.as_view(),
         name='add_jocke'),
    path('eyes/<int:jocke_id>', views.JockeEyes.as_view(), name='eyes'),
]
