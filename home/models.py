from django.db import models

class BusinessMessage(models.Model):
    message = models.CharField(max_length=255)
    image = models.ImageField(upload_to='messages/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.message
    


