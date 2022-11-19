from rest_framework import permissions
from artists.models import Artist


class IsArtist(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return isinstance(obj, Artist)
