from django.db import IntegrityError
from rest_framework import serializers
from .models import Favourite

class FavouriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Favourite
        fields = [
            'id', 'owner', 'is_owner','recipe',
        ]

    def create(self, validated_error):
        try:
            return super().create(validated_error)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
