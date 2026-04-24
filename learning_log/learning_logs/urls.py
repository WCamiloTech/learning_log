"""Define padrões de URL para learning_logs"""
from . import views
from django.urls import path

# Adicione esta linha:
app_name = 'learning_logs'

urlpatterns = [
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # Página para adicionar um novo assunto
    path("new_topic", views.new_topic, name="new_topic"),
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
]
