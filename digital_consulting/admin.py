from django.contrib import admin
from .models import DigitalConsulting
from django_summernote.admin import SummernoteModelAdmin

@admin.register(DigitalConsulting)
class DigitalConsultingAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_at')
    summernote_fields = ('overview',)
    
    fieldsets = (
        ('Page Header', {
            'fields': ('title', 'image')
        }),
        ('Overview Section', {
            'fields': ('overview',)
        }),
        
    )

