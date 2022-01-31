""" URLs for Wellbeing app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('wellbeing/<int:author_id>', views.PostMood.as_view(), name='post_mood'),
    path('wellbeing/<int:author_id>/<str:mood>', views.ClickMood.as_view(), name='click_mood'),
    path('tired', views.get_tired_page, name='tired'),
    path('bored', views.get_bored_page, name='bored'),
    path('happy', views.get_happy_page, name='happy'),
    path('stressed', views.get_stressed_page, name='stressed'),
]
