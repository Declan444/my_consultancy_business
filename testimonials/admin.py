from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'created_at')
    search_fields = ('name', 'company')
    ordering = ('-created_at',)
