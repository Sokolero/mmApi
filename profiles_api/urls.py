from django.urls import path
from rest_framework import routers
from . import views

# urlpatterns = [
#     path('ho/', views.ObjectViewSet.as_view({'get':'list'}), name='ho'),
# ]
urlpatterns = []

router = routers.DefaultRouter()
router.register(r'objects', views.ObjectViewSet, basename='objects')
router.register(r'gallerys', views.GalleryViewSet, basename='gallerys')

urlpatterns += router.urls
