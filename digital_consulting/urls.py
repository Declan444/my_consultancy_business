from django.urls import path
from . import views

app_name = 'digital_consulting'

urlpatterns = [
    path('', views.digital_consulting_view, name='digital_consulting_view'),
]