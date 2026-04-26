"""Define padrões de URL para users"""
from django.contrib.auth.views import LoginView
from . import views
from django.urls import path

urlpatterns = [
    # Página de login
    # path("login/", login, {'template_name':"users/login.html"}, name="login"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
]


