from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser

from api.models import Object, Category, Gallery
from users.models import CustomUser
from users.permissions import IsMasterPermission, IsOwnerPermission

from .serializers import ObjectSerializer, GallerySerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'objects': reverse('object-list', request=request, format=format),
        'gallerys': reverse('gallery-list', request=request, format=format),
    })


class ObjectList(generics.ListCreateAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [IsAuthenticated, IsMasterPermission,]

    def create(self, request, *args, **kwargs):
        serializer = ObjectSerializer(data=request.data, context={'request': request})
        # import pdb; pdb.set_trace()
        user = request.user
        if serializer.is_valid():
            validated_data = serializer.validated_data
            files = validated_data.pop('files')
            selected_categorys = validated_data.pop('selected_categorys')
            object = Object.objects.create(
                user=user,
                X=validated_data.get('X'),
                Y=validated_data.get('Y'),
            )
            categorys = [Category.objects.get(category_name=category) for category in selected_categorys]
            object.categorys.set(categorys)
            gallerys = [Gallery(object=object, photo=file) for file in files]
            Gallery.objects.bulk_create(gallerys)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Object.objects.filter(user=self.request.user)
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class ObjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [IsAuthenticated, IsMasterPermission, IsOwnerPermission]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def partial_update(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        obj = Object.objects.get(pk=self.kwargs['pk'])
        serializer = ObjectSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            validated_data = serializer.validated_data
            files = validated_data.pop('files')
            obj.X = validated_data.get('X')
            obj.Y = validated_data.get('Y')
            categorys = [Category.objects.get(category_name=category_name) for category_name in validated_data.get('categorys')]
            obj.categorys.set(categorys)
            obj.gallerys.all().delete()
            gallerys = [Gallery.objects.create(object=obj, photo=file) for file in files]
            obj.gallerys.set(gallerys)
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GalleryList(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

#############Deprecated
# Create your views here.
# class ObjectView(APIView):
#
#     # queryset = Object.objects.all()
#     # # permission_classes = [IsAuthenticated]
#     # serializer_class = ObjectSerializer
#
#     def post(self, request, *args, **kwargs):
#         import pdb; pdb.set_trace
#         print(request.data)
#         user = request.user
#         serializer = ObjectSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         validated_data = serializer.validated_data
#         files = validated_data.pop('files')
#
#         object = Object.objects.create(
#             user=user,
#             X=validated_data.get('X'),
#             Y=validated_data.get('Y'),
#         )
#         categorys = [Category.objects.get(category_name=cat_name) for cat_name in validated_data.get('categorys')]
#         object.categorys.set(categorys)
#         gallerys = [Gallery(object=object, photo=file) for file in files]
#         Gallery.objects.bulk_create(gallerys)
#         return Response(serializer.data)
#
#
# class ObjectDetailView(generics.RetrieveAPIView):
#     queryset = Object.objects.all()
#     serializer_class = ObjectListSerializer
#
# # ==========
# class ObjectListView(generics.ListAPIView):
#     queryset = Object.objects.all()
#     # permission_classes = [IsAuthenticated, IsMasterPermission]
#     serializer_class = ObjectListSerializer
#
#     def get_queryset(self):
#         print(self.request.data)
#         return Object.objects.filter(user_id=self.request.user.id)
#
#
# class GalleryListView(generics.ListAPIView):
#     queryset = Gallery.objects.all()
#     serializer_class = GallerySerializer
#
#
# class GalleryDetailView(generics.RetrieveAPIView):
# #     queryset = Gallery.objects.all()
#     serializer_class = GallerySerializer
