"""Define padrões de URL para learning_logs"""
from . import views
from django.urls import path

# Adicione esta linha:
app_name = 'learning_logs'

urlpatterns = [
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
]
