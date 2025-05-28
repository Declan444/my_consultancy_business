from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_home, name='contact'),
]