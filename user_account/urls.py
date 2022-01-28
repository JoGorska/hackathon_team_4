from django.urls import path
from django.contrib.auth import views as auth_views
from user_account.views import RegisterUserView
from . import views

app_name = "user_account"

urlpatterns = [
    path(
        "login",
        auth_views.LoginView.as_view(template_name="user_account/login.html"),
        name="login",
    ),
    path("register", RegisterUserView.as_view(), name="register"),
]