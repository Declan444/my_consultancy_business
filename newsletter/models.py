from django.db import models


class NewsletterSubscriber(models.Model):
    """
    Model representing Newsletter Subscribers.

    """

    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"

