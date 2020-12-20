from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser

from .serializers import ObjectSerializer, GallerySerializer, ObjectListSerializer, GalleryDetailSerializer
from api.models import Object, Category, Gallery
from users.models import CustomUser
from users.permissions import IsMasterPermission, IsOwnerPermission


# Create your views here.
class ObjectView(APIView):

    # queryset = Object.objects.all()
    # # permission_classes = [IsAuthenticated]
    # serializer_class = ObjectSerializer

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace
        print(request.data)
        user = request.user
        serializer = ObjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        files = validated_data.pop('files')

        object = Object.objects.create(
            user=user,
            X=validated_data.get('X'),
            Y=validated_data.get('Y'),
        )
        categorys = [Category.objects.get(category_name=cat_name) for cat_name in validated_data.get('categorys')]
        object.categorys.set(categorys)
        gallerys = [Gallery(object=object, photo=file) for file in files]
        Gallery.objects.bulk_create(gallerys)
        return Response(serializer.data)


class ObjectDetailView(generics.RetrieveAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectListSerializer

# ==========
class ObjectListView(generics.ListAPIView):
    queryset = Object.objects.all()
    # permission_classes = [IsAuthenticated, IsMasterPermission]
    serializer_class = ObjectListSerializer

    def get_queryset(self):
        print(self.request.data)
        return Object.objects.filter(user_id=self.request.user.id)


class GalleryListView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryDetailView(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
