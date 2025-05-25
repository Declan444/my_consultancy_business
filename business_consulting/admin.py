from django.contrib import admin
from .models import BusinessConsulting

@admin.register(BusinessConsulting)
class BusinessConsultingAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    
    fieldsets = (
        ('Page Header', {
            'fields': ('title', 'image')
        }),
        ('Overview Section', {
            'fields': ('overview',)
        }),
        
    )
