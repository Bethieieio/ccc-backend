"""favourites serializer class"""
from django.db import IntegrityError
from rest_framework import serializers
from .models import Favourite

class FavouriteSerializer(serializers.ModelSerializer):
    """favourites serialzier for serializing favourites"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """is owner property for determining if favourite belongs ro current logged in user"""
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        """meta class for metaing classes"""
        model = Favourite
        fields = [
            'id', 'owner', 'is_owner','recipe',
        ]

    def create(self, validated_data):

        try:
            return super().create(validated_data)
        except IntegrityError as exc:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            }) from exc
