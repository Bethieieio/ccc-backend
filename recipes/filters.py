import django_filters
from categories.models import Category
from .models import Recipe
from django.db.models import Q

class RecipeFilter(django_filters.FilterSet):
    categories = django_filters.ModelMultipleChoiceFilter(
        field_name='categories__name',
        to_field_name='name',
        lookup_expr='contains',
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Recipe
        fields = ['categories']
