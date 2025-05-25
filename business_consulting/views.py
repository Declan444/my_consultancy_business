from django.shortcuts import render
from .models import BusinessConsulting

def business_consulting_view(request):
    businessconsulting_content = BusinessConsulting.objects.first()  #
    return render(request, 'businessconsulting/businessconsulting.html', {'businessconsulting': businessconsulting_content})
