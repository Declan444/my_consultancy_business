from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)  # Name of the person giving the testimonial
    company = models.CharField(max_length=150, blank=True, null=True)  # Company name (optional)
    text = models.TextField()  # Testimonial text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for ordering

    def __str__(self):
        return self.name
