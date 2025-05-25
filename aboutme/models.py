from django.db import models
from django_summernote.fields import SummernoteTextField

class AboutMe(models.Model):
    title = models.CharField(max_length=200, help_text="Title for the About Me page")
    content = SummernoteTextField(help_text="Main content for the About Me page (will be used as overview)", blank=True)
    image = models.ImageField(upload_to='aboutme/', blank=True, null=True, help_text="Optional image for the About Me page")
    updated_at = models.DateTimeField(auto_now=True)
    
    # New fields for accordion sections
    overview = SummernoteTextField(help_text="Overview text displayed next to image", blank=True)
    
    section1_title = models.CharField(max_length=200, default="Section 1", help_text="Title for first section")
    section1_content = SummernoteTextField(blank=True, help_text="Content for first section")
    
    section2_title = models.CharField(max_length=200, default="Section 2", help_text="Title for second section")
    section2_content = SummernoteTextField(blank=True, help_text="Content for second section")
    
    section3_title = models.CharField(max_length=200, default="Section 3", help_text="Title for third section")
    section3_content = SummernoteTextField(blank=True, help_text="Content for third section")
    
    section4_title = models.CharField(max_length=200, default="Section 4", help_text="Title for fourth section")
    section4_content = SummernoteTextField(blank=True, help_text="Content for fourth section")
    
    section5_title = models.CharField(max_length=200, default="Section 5", help_text="Title for fifth section")
    section5_content = SummernoteTextField(blank=True, help_text="Content for fifth section")

    def __str__(self):
        return self.title
