from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    EVENT_CHOICES = [
        ('Wedding', 'Wedding'),
        ('Corporate', 'Corporate Event'),
        ('Birthday', 'Birthday Party'),
        ('Exhibition', 'Exhibition'),
        ('Concert', 'Concert'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
