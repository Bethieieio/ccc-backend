from dj_rest_auth.serializers import UserDetailsSerializer

class CurrentUserSerializer(UserDetailsSerializer):
    """Serialisers user for JWT calls """

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields
