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
import requests


@api_view(["GET"])
def consented_contacts(request):
    messages = ContactMessage.objects.filter(consent=True).order_by("-created_at")
    serializer = ContactMessageSerializer(messages, many=True)
    return Response(serializer.data)


def contact_home(request):
    confirmation_message = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send confirmation email to user (HTML formatted)
            html_message = f"""
            <html>
            <body style='font-family: Arial, sans-serif; background: #f9f9f9; padding: 20px;'>
                <div style='max-width: 600px; margin: auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); padding: 30px;'>
                    <h2 style='color: #445261; text-align: center;'>Thank You for Contacting DL Consultancy</h2>
                    <p>Hi <strong>{contact.full_name}</strong>,</p>
                    <p>Thank you for getting in touch! We've received your message and will reply as soon as we can.</p>
                    <hr style='border: none; border-top: 1px solid #eee;'>
                    <h4 style='color: #445261;'>Your Message:</h4>
                    <p><strong>Subject:</strong> {contact.subject}</p>
                    <p><strong>Message:</strong><br>{contact.message}</p>
                    <hr style='border: none; border-top: 1px solid #eee;'>
                    <p style='font-size: 0.95em; color: #888;'>
                        Declan Lenahan<br>
                        DL | Business and Digital Consultant<br>
                        <a href='mailto:laresearchlabs@gmail.com' style='color: #445261;'>laresearchlabs@gmail.com</a><br>
                        <a href='tel:+353868934130' style='color: #445261;'>+353 868934130</a>
                    </p>
                </div>
            </body>
            </html>
            """
            send_mail(
                subject="Thanks for contacting DL Consultancy",
                message=f"Hi {contact.full_name},\n\nThanks for getting in touch. We've received your message:\n\n{contact.message}\n\nWe'll reply as soon as we can.\n\nDeclan",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
                fail_silently=False,
                html_message=html_message,
            )

            # If consented, trigger the webhook
            if contact.consent:
                try:
                    response = requests.post(
                        "https://dlconsultant.app.n8n.cloud/webhook/lead-intake",
                        json={
                            "full_name": contact.full_name,
                            "email": contact.email,
                            "subject": contact.subject,
                            "message": contact.message,
                            "created_at": str(contact.created_at),
                        },
                        timeout=5,
                    )
                    print(f"Webhook response: {response.status_code} - {response.text}")
                except requests.exceptions.RequestException as e:
                    print(f"Failed to trigger n8n webhook: {e}")

            # Notify admin
            admin_subject = f"New Contact Message from {contact.full_name}"
            admin_body = f"""
You received a new contact message:

Name: {contact.full_name}
Email: {contact.email}
Subject: {contact.subject}
Message:
{contact.message}
            """
            send_mail(
                admin_subject,
                admin_body,
                settings.DEFAULT_FROM_EMAIL,
                [admin[1] for admin in settings.ADMINS] + ["laresearchlabs@gmail.com"],
                fail_silently=False,
            )

            confirmation_message = (
                "Your message has been sent. We will be in touch soon."
            )
            return render(
                request,
                "contact/contact.html",
                {"form": ContactForm(), "confirmation_message": confirmation_message},
            )
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})


@csrf_exempt
def log_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            recipient = data.get("recipient")
            subject = data.get("subject", "No Subject")
            message = data.get("message", "")

            if not recipient:
                return JsonResponse(
                    {"error": "Recipient email is required"}, status=400
                )

            EmailLog.objects.create(
                recipient=recipient,
                subject=subject,
                message=message,
            )
            return JsonResponse({"status": "logged"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "POST request required"}, status=405)
