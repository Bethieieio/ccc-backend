"""rating serializer"""
from django.db import IntegrityError
from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """rating serializer class for serializing raitings"""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        """is owner property for determining if rating belongd to loggied in  user"""
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        """meta class"""
        model = Rating
        fields = [
            'id', 'owner', 'is_owner','recipe', 'value'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError as exc:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            }) from exc

    def validate_value(self, value):
        """validating rating value is bwtween 1 and 5"""
        if value > 5 or value < 1:
            raise serializers.ValidationError('Rating must be between 1 - 5')

        return value
