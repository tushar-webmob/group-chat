from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
     path('rooms/', views.rooms, name='rooms'),
     path('<slug:slug>/', views.room, name='room')
]

