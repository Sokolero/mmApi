from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CustomUserSerializer, CreateMasterSerializer
from .models import CustomUser

# Create your views here.
#Registration of the new user
class CustomUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

#GET current user profile datas
class CustomUserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({
            "id": user.id,
            "is_master": user.is_master,
            "email": user.email,
        })

# UPDATE profile of the current authenticated user to change on
# his status is_master=True
class CreateMasterView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateMasterSerializer

    def update(self, request, *args, **kwawrgs):
        user = request.user
        user.is_master = True
        serializer = CreateMasterSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
