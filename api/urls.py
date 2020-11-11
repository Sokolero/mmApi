from django.urls import path
from . import views

urlpatterns = [
    path('objects/', views.ObjectListView.as_view(), name='objectlist'),
    path('object/', views.ObjectManageView.as_view(), name='object'),
    path('masters/', views.MasterListCreateView.as_view(), name='masters'),
    path('categorys/', views.CategoryList.as_view(), name='categorys'),
]
