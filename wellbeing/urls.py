from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoodView.as_view(), name='home'),
]