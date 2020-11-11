from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomUserView, CustomUserMeView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('registration/', CustomUserView.as_view(), name='registration'),
    path('me/', CustomUserMeView.as_view(), name='me'),
]
