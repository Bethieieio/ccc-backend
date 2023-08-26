"""permissions"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """class to chec that object belongs to signed in user"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    