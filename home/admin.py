from django.contrib import admin
from django.utils.html import format_html
from .models import BusinessMessage

@admin.register(BusinessMessage)
class BusinessMessageAdmin(admin.ModelAdmin):
    list_display = ("message", "is_active", "image_preview")  # Add image_preview to the list display
    list_filter = ("is_active",)
    search_fields = ("message",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;">', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"
