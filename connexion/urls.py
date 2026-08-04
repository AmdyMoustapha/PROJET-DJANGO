from django.urls import path
from . import views

urlpatterns = [
    path('', views.connexion_view, name = 'connexion'),
]