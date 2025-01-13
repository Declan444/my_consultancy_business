from django.shortcuts import render
from .models import AboutMe

def about_me_view(request):
    aboutme_content = AboutMe.objects.first()  # Assuming there will be only one AboutMe entry
    return render(request, 'aboutme/aboutme.html', {'aboutme': aboutme_content})
