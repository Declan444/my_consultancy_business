from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at', 'consent')
    search_fields = ('full_name', 'email', 'subject', 'message', 'consent')
    list_filter = ('created_at', 'consent')
    ordering = ('-created_at',)
