from django.contrib import admin
from .models import Question

# Register the Question model
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')  # Display these fields in the admin list view
    search_fields = ('question_text',)      # Add a search bar to find questions by text