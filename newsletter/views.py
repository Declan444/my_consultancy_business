from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSubscriptionForm


def subscribe_to_newsletter(request):
    if request.method == "POST":
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thank you for subscribing to our newsletter!"
            )
        else:
            messages.error(
                request, "This email address is already"
                         " subscribed or invalid."
            )
        return redirect("index1")
    else:
        form = NewsletterSubscriptionForm()
    return render(request, "newsletter/signup.html", {"form": form})
