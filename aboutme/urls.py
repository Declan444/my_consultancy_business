from django.urls import path
from . import views

app_name = 'aboutme'

urlpatterns = [
    path('', views.about_me_view, name='about_me_view'),
]