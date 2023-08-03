from django.db import IntegrityError
from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Rating
        fields = [
            'id', 'owner', 'is_owner','recipe', 'value'
        ]

    def create(self, validated_error):
        try:
            return super().create(validated_error)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
        
    def validate_value(self, value):
        if value > 5 or value < 1:
            raise serializers.ValidationError('Rating must be between 1 - 5')
        return value