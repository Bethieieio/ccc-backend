"""recipe filters file for recipe filter class"""
import django_filters
from categories.models import Category
from .models import Recipe

class RecipeFilter(django_filters.FilterSet):
    """recipe filters to filter recipe queries"""
    categories = django_filters.ModelMultipleChoiceFilter(
        field_name='categories__name',
        to_field_name='name',
        lookup_expr='contains',
        queryset=Category.objects.all(),
    )

    class Meta:
        """meta data fpr recipe filters"""
        model = Recipe
        fields = ['categories']
