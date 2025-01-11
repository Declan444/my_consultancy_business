from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("", views.index, name="index1"),
    path("get-random-message/", views.get_random_message, name="get_random_message"),
    path("testimonials/", include("testimonials.urls")),
    
]
