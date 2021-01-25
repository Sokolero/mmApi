from django.urls import path, include
# from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('objects/', views.ObjectList.as_view(), name='object-list'),
    path('objects/<int:pk>/', views.ObjectDetail.as_view(), name='object-detail'),
    path('gallerys/', views.GalleryList.as_view(), name='gallery-list'),
    path('gallery/<int:pk>/', views.GalleryDetail.as_view(), name='gallery-detail'),
])
