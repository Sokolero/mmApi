from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import ObjectSerializer, GallerySerializer
from api.models import Object, Category, Gallery
from users.models import CustomUser
from users.permissions import IsMasterPermission, IsOwnerPermission


# Create your views here.
class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [
        IsAuthenticated,
        IsMasterPermission,
    ]

    def create(self, request):
        user = request.user
        serializer = ObjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        object = Object.objects.get(pk=pk)
        serializer = ObjectSerializer(object, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        return Object.objects.filter(user__pk=self.request.user.pk)


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    permission_classes = [IsAuthenticated, IsMasterPermission]
    serializer_class = GallerySerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request):
        user = request.user
        serializer = GallerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data)

    def get_queryset(self):
        return Gallery.objects.filter(user__pk=self.request.user.pk)
