"""Define padrões de URL para learning_logs"""
from . import views
from django.urls import path

# Adicione esta linha:
app_name = 'learning_logs'

urlpatterns = [
    # Página inicial
    path("", views.index, name="index"),
]
