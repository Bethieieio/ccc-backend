"""favourites list file"""
from rest_framework import generics, permissions
from ccc_backend.permissions import IsOwnerOrReadOnly
from .serializers import FavouriteSerializer
from .models import Favourite

class FavouriteList(generics.ListCreateAPIView):
    """favourite list class for list create API views"""
    serializer_class = FavouriteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Favourite.objects.all()

    def perform_create(self, serializer):
        """customising perform create to add current logged in user to serializer"""
        serializer.save(owner=self.request.user)

class FavouriteDetails(generics.RetrieveDestroyAPIView):
    """favourite details for retrieeve and destory APAI Views"""
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
