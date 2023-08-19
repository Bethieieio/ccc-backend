from django.db import models

class Category(models.Model):
    """Categories model"""
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "categories"

# class RecipeCategories(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


#     class Meta:
#         unique_together = ['recipe', 'category']

#     def __str__(self):
#         return "recipe_categories"

