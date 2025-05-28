from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    consent = forms.BooleanField(required=False)
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'subject', 'message', 'consent']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_honeypot(self):
        data = self.cleaned_data['honeypot']
        if data:
            raise forms.ValidationError("Spam detected.")
        return data