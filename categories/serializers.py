"""catagory serilaizer class for serializing categories."""
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    """category serializer for catagory model"""
    class Meta:
        """meta class for catagory serializer"""
        model = Category
        fields = [
            'name',
            'id',
        ]
