from rest_framework import generics, permissions
from ccc_backend.permissions import IsOwnerOrReadOnly
from .serializers import FavouriteSerializer
from .models import Favourite

class FavouriteList(generics.ListCreateAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Favourite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FavouriteDetails(generics.RetrieveDestroyAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]

