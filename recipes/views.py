from rest_framework import generics, permissions
from ccc_backend.permissions import IsOwnerOrReadOnly
from .serializers import RecipeSerializer
from .models import Recipe
from categories.models import Category
import json
from rest_framework.response import Response
from .filters import RecipeFilter

class RecipeList(generics.ListCreateAPIView):
    filterset_class = RecipeFilter
    serializer_class = RecipeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Recipe.objects.all()

    def create(self, request, *args, **kwargs):
        categories_data = json.loads(request.data.get('categories'))

        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        recipe = self.perform_create(serializer)

        for category_data in categories_data:
            category_name = category_data.get('name')
            category, _ = Category.objects.get_or_create(name=category_name)
            recipe.categories.add(category)

        return Response(serializer.data)


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class RecipeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    queryset = Recipe.objects.all()

    def update(self, request, *args, **kwargs):
        categories_data = json.loads(request.data.get('categories'))

        partial = kwargs.pop('partial', False)
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        recipe.categories.clear()

        for category_data in categories_data:
            category_name = category_data.get('name')
            category, _ = Category.objects.get_or_create(name=category_name)
            recipe.categories.add(category)

        return Response(serializer.data)
