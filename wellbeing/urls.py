from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('wellbeing/<int:author_id>', views.PostMood.as_view(), name='post_mood'),
]