"""rating list class"""
from rest_framework import generics, permissions
from ccc_backend.permissions import IsOwnerOrReadOnly
from .serializers import RatingSerializer
from .models import Rating

class RatingList(generics.ListCreateAPIView):
    """class for rating rating list in create"""
    serializer_class = RatingSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RatingDetails(generics.RetrieveDestroyAPIView):
    """rating deatails class for single rating fetach and delete"""
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
