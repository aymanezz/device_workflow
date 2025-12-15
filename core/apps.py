from django.apps import AppConfig


class CoreConfig(AppConfig):
default_auto_field = 'django.db.models.BigAutoField'
name = 'core'


# core/urls.py
from django.urls import path
from core import views


urlpatterns = [
path('', views.home, name='home'),
]