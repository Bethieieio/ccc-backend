from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from recipes.models import Recipe

class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        unique_together = ['owner', 'recipe']
        
    def __str__(self):
        return f"{self.owner}'s rating"
    
def create_favourite(instance, created, **kwargs):
    if created:
        Rating.objects.create(owner=instance)

post_save.connect(create_favourite, sender=User)