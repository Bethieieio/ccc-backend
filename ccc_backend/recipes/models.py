from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

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

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s recipe"

def create_recipe(instance, created, **kwargs):
    if created:
        Recipe.objects.create(owner=instance)

post_save.connect(create_recipe, sender=User)