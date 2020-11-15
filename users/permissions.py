from rest_framework import permissions

# The custom permissions classes
class IsMasterPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_master


class IsOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        user_id = request.user.id
        changed_user_id = request.data['user']
        return changed_user_id == user_id
