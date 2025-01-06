from django.shortcuts import render
from django.http import JsonResponse
from .models import BusinessMessage
import random

def index(request):
    return render(request, "home/index.html")

def get_random_message(request):
    print("Request received for random message!")  # Debug
    active_messages = BusinessMessage.objects.filter(is_active=True)
    print("Active messages count:", active_messages.count())  # Debug
    
    if active_messages.exists():
        random_message = random.choice(active_messages)
        image_url = random_message.image.url if random_message.image else None
        print("Random message selected:", random_message.message)  # Debug
        return JsonResponse({
            'message': random_message.message,
            'image_url': image_url  # Send the image URL along with the message
        })
    else:
        print("No active messages found!")  # Debug
        return JsonResponse({'message': 'No messages available at the moment.'})

