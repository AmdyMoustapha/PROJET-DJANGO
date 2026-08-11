from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscription_view, name = 'inscription'),
]