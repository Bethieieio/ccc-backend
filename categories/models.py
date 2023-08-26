"""category model file"""
from django.db import models

class Category(models.Model):
    """Categories model"""
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "categories"
