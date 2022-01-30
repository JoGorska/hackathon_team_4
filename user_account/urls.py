""" URLs for user_account app """
# pylint: disable=unused-import
from django.urls import path
from django.contrib.auth import views as auth_views
from user_account.views import RegisterUserView
from . import views

APP_NAME = "user_account"

urlpatterns = [
    path(
        "login",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("register", views.RegisterUserView.as_view(), name="register"),
]
