from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=False)
    ingredients = models.TextField(blank=False)
    description = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='images/', default='../default_recipe_image', blank=True
    )
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s recipe"
