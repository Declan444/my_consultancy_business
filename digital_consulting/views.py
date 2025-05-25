from django.shortcuts import render
from .models import DigitalConsulting

def digital_consulting_view(request):
    digitalconsulting_content = DigitalConsulting.objects.first()  #
    return render(request, 'digitalconsulting/digitalconsulting.html', {'digitalconsulting': digitalconsulting_content})
