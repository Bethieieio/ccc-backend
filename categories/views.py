"""category list view file for category list class"""
from rest_framework import generics, permissions
from .models import Category

class CategoryList(generics.ListAPIView):
    """API view for displaying category via API call"""
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Category.objects.all()
