from django.db import models

# Create your models here.
class Bedrooms(models.Model):
    language = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    keywords = models.CharField(max_length=255, blank=True)