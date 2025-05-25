from django.urls import path
from . import views

app_name = 'business_consulting'

urlpatterns = [
    path('', views.business_consulting_view, name='business_consulting_view'),
]