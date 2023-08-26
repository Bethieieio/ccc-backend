"""current user serializer file"""
from dj_rest_auth.serializers import UserDetailsSerializer

class CurrentUserSerializer(UserDetailsSerializer):
    """Serialisers user for JWT calls """

    class Meta(UserDetailsSerializer.Meta):
        """meta class for current user serializer"""
        fields = UserDetailsSerializer.Meta.fields
