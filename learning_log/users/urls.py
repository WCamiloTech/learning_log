"""Define padrões de URL para users"""
from django.contrib.auth.views import LoginView
from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    # Página de login
    # path("login/", login, {'template_name':"users/login.html"}, name="login"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
    # Página de cadastro
    path("register/", views.register, name="register"),
]


