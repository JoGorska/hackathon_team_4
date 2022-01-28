from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('', views.PostMood.as_view(), name='post_mood'),
]