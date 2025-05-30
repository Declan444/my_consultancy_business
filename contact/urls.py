from django.urls import path
from . import views
from .views import consented_contacts

urlpatterns = [
    path('', views.contact_home, name='contact'),
    path('api/consented/', consented_contacts, name='consented_contacts'),
    path("api/log-email/", views.log_email, name="log_email"),
]