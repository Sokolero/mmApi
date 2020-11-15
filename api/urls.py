from django.urls import path
from . import views

urlpatterns = [
    path('objects/', views.ObjectListView.as_view(), name='objects'),
    path('categorys/', views.CategoryListView.as_view(), name='categorys'),
    path('masters/', views.MasterListView.as_view(), name='masters'),
    path('gallerys/', views.GalleryListView.as_view(), name='gallerys'),
]
