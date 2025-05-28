from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import EmailLog
import json

@api_view(['GET'])
def consented_contacts(request):
    messages = ContactMessage.objects.filter(consent=True).order_by('-created_at')
    serializer = ContactMessageSerializer(messages, many=True)
    return Response(serializer.data)

def contact_home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            send_mail(
                subject="Thanks for contacting DL Consultancy",
                message=f"Hi {contact_message.full_name},\n\nThanks for getting in touch. We’ve received your message:\n\n{contact_message.message}\n\nWe'll reply as soon as we can.\n\nDeclan",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact_message.email],
                fail_silently=False,
)

            # Send email notification to admin
            subject = f"New Contact Message from {contact_message.full_name}"
            body = f"""
You received a new contact message:

Name: {contact_message.full_name}
Email: {contact_message.email}
Subject: {contact_message.subject}
Message:
{contact_message.message}
            """
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [admin[1] for admin in settings.ADMINS] + ['laresearchlabs@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent. We will be in touch soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

@csrf_exempt
def log_email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        EmailLog.objects.create(
            recipient=data.get("recipient"),
            subject=data.get("subject"),
            message=data.get("message"),
        )
        return JsonResponse({"status": "logged"})