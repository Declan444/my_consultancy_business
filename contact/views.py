from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings

def contact_home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

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