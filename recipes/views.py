from rest_framework import generics, permissions
from ccc_backend.permissions import IsOwnerOrReadOnly
from .serializers import RecipeSerializer

class RecipeList(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RecipeDetails(generics.RetrieveDestroyAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]
