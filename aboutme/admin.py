from django.contrib import admin
from .models import AboutMe

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    
    fieldsets = (
        ('Page Header', {
            'fields': ('title', 'image')
        }),
        ('Overview Section', {
            'fields': ('overview',)
        }),
        ('Section 1', {
            'fields': ('section1_title', 'section1_content')
        }),
        ('Section 2', {
            'fields': ('section2_title', 'section2_content')
        }),
        ('Section 3', {
            'fields': ('section3_title', 'section3_content')
        }),
        ('Section 4', {
            'fields': ('section4_title', 'section4_content')
        }),
        ('Section 5', {
            'fields': ('section5_title', 'section5_content')
        }),
    )