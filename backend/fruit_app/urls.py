from django.urls import path
from .views import send_fruits, info


urlpatterns = [
    path('', send_fruits),
    path('info/', info, name="info"),
]
