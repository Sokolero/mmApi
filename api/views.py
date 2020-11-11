from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import (ObjectSerializer, ObjectListSerializer,
 MasterSerializer, CategorySerializer)
from .models import Object, Master, Category

# Create your views here.
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


class ObjectListView(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectListSerializer
    permission_classes =  [AllowAny]


class ObjectManageView(generics.CreateAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [IsAuthenticated, IsMasterPermission, IsOwnerPermission]


class MasterListCreateView(generics.ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]



class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
