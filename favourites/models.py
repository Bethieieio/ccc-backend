from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Favourite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'recipe']
        
    def __str__(self):
        return f"{self.owner}'s favourite"
