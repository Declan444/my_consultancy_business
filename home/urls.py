from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get-random-message/", views.get_random_message, name="get_random_message"),
    
]
