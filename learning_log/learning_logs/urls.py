"""Define padrões de URL para learning_logs"""
from . import views
from django.urls import path

urlpatterns = [
    # Página inicial
    path("", views.index, name="index"),
]
