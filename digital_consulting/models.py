from django.db import models
from django_summernote.fields import SummernoteTextField

class DigitalConsulting(models.Model):
    title = models.CharField(max_length=200, help_text="Title for the Digital Consulting page")
    
    overview = SummernoteTextField(help_text="Overview text displayed next to image", blank=True)
    image = models.ImageField(upload_to='digitalconsulting/', blank=True, null=True, help_text="Optional image for the Digital Consulting page")
    updated_at = models.DateTimeField(auto_now=True)
     # New fields for accordion sections
    
    
    

    def __str__(self):
        return self.title
