"""rating model file"""
from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Rating(models.Model):
    """Rating model class for ratings"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField()

    class Meta:
        """Meta class for rating model"""
        unique_together = ['owner', 'recipe']

    def __str__(self):
        return f"{self.owner}'s rating"
