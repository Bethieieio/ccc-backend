"""recipe serializers for recipe serializer class"""
from rest_framework import serializers
from categories.serializers import CategorySerializer
from ratings.serializers import RatingSerializer
from favourites.serializers import FavouriteSerializer
from .models import Recipe



class RecipeSerializer(serializers.ModelSerializer):
    """recipe serializer for recipe output data"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True, read_only=True)
    favourites = FavouriteSerializer(read_only=True, many=True)
    ratings = RatingSerializer(many=True, read_only=True)

    def validate_image(self, value):
        """for validating image size and resolution"""
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
        """is owner property for displaying if recipe belongs to current logged in user """
        request = self.context['request']
        return request.user == obj.owner

    def get_average_rating(self, instance):
        """average rating property for calculating recipe raitng"""
        ratings = instance.ratings.all()
        if ratings:
            rating_values = [rating.value for rating in ratings]
            average_rating = sum(rating_values) / len(rating_values)
            return round(average_rating, 1)
        return None

    class Meta:
        """meta class for recipe serializer"""
        model = Recipe
        fields = [
            'id', 'owner', 'is_owner',
            'created_at', 'updated_at',
            'title', 'description', 'image', 
            'ingredients', 'instructions', 'categories', 'favourites', 'average_rating', 'ratings',
        ]
