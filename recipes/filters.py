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
    isOwner = django_filters.BooleanFilter(
        field_name='recipe__owner',
        method="filter_is_owner",
        label="Is Owner",
    )
    isFavourited = django_filters.BooleanFilter(
        field_name="recipe__favourite",
        method="filter_is_favourite",
        label="Is Favourited",
    )

    def filter_is_owner(self, queryset, name, value):
        """Filter by current signed in user"""
        if value:
            user = self.request.user
            return queryset.filter(owner=user.id).distinct()
        return queryset

    def filter_is_favourite(self, queryset, name, value):
        """Filter favourited recipes"""
        if value:
            user = self.request.user
            return queryset.filter(favourites__owner=user.id).distinct()
        return queryset

    class Meta:
        """meta data fpr recipe filters"""
        model = Recipe
        fields = ['categories']
