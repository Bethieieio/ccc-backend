from rest_framework import serializers
from categories.serializers import CategorySerializer
from categories.models import Category
from .models import Recipe
from favourites.serializers import FavouriteSerializer


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True, read_only=True)
    favourites = FavouriteSerializer(read_only=True, many=True)

    def validate_empty_values(self, data):
        return super().validate_empty_values(data)

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'is_owner',
            'created_at', 'updated_at',
            'title', 'description', 'image', 
            'ingredients', 'instructions', 'categories', 'favourites',
        ]
