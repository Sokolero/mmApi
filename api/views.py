from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    ObjectListSerializer,
    CategorySerializer,
    GallerySerializer,
    MasterListSerializer,
    )
from .models import Object, Category, Gallery
from users.permissions import IsMasterPermission, IsOwnerPermission
from users.models import CustomUser

# Create your views here.
#GET object list - for all users
class ObjectListView(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectListSerializer

#GET category list - for all users
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#GET list of users that have 'is_master=True'
class MasterListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(is_master=True)
    serializer_class = MasterListSerializer


class GalleryListView(generics.ListAPIView):
    serializer_class = GallerySerializer

    def get_queryset(self):
        return Gallery.objects.filter()
