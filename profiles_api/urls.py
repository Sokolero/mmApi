from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('create_object/', views.ObjectView.as_view(), name='create_object'),
    path('objects/', views.ObjectListView.as_view(), name='object-list'),
    path('objects/<int:pk>/', views.ObjectDetailView.as_view(), name='object-detail'),
    path('gallerys/<int:pk>/', views.GalleryDetailView.as_view(), name='gallery-detail'),
    path('gallerys/', views.GalleryListView.as_view(), name='gallery-list'),
])

router = routers.DefaultRouter()
# router.register(r'objects', views.ObjectViewSet, basename='objects')
# router.register(r'gallerys', views.GalleryViewSet, basename='gallerys')

urlpatterns += router.urls
