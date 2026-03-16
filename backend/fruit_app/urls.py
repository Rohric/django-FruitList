from django.urls import path
from .views import send_fruits


urspatterns = [
    path('', send_fruits),
]
