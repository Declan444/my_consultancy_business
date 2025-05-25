# quiz/models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text
    
class CustomerRequest(models.Model):
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
