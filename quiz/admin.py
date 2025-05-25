from django.contrib import admin
from .models import Question, CustomerRequest

# Register the Question model
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')  # Display these fields in the admin list view
    search_fields = ('question_text',)      # Add a search bar to find questions by text

# Register the CustomerRequest model
@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'submitted_at')  # Display these fields in the admin list view
    search_fields = ('email',)                      # Add a search bar to find emails
    ordering = ('-submitted_at',)                   # Order by most recent submissions