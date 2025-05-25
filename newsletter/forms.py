from django import forms
from .models import NewsletterSubscriber


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control mx-auto",
                    "placeholder": "Enter your email address",
                    "autocomplete": "email",
                }
            ),
        }