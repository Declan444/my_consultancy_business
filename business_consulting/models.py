from django.db import models
from django_summernote.fields import SummernoteTextField

class BusinessConsulting(models.Model):
    title = models.CharField(max_length=200, help_text="Title for the Business Consulting page")
    content = models.TextField(help_text="Main content for the Business Consulting page (will be used as overview)", blank=True)
    image = models.ImageField(upload_to='businessconsulting/', blank=True, null=True, help_text="Optional image for the Business Consulting page")
    updated_at = models.DateTimeField(auto_now=True)
     # New fields for accordion sections
    
    overview = SummernoteTextField(help_text="Overview text displayed next to image", blank=True)
    
    

    def __str__(self):
        return self.title
