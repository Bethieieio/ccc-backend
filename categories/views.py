from rest_framework import generics, permissions
from .models import Category

class CategoryList(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Category.objects.all()
