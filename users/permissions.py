from rest_framework import permissions

# The custom permissions classes
class IsMasterPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_master


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj.user
