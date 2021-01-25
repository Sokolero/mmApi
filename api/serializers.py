from rest_framework import serializers
from .models import Object, Category, Gallery
from users.models import CustomUser


class ObjectListSerializer(serializers.ModelSerializer):
    X = serializers.CharField(max_length=10)
    Y = serializers.CharField(max_length=10)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    date_of_creation = serializers.DateTimeField(read_only=True)
    categorys = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Object
        fields = ('id', 'X', 'Y', 'user', 'date_of_creation', 'categorys')


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = ('id', 'category_name')

class MasterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_master', 'first_name', 'last_name']


class GallerySerializer(serializers.ModelSerializer):
    object = serializers.PrimaryKeyRelatedField(queryset=Object.objects.all())

    class Meta:
        model = Gallery
        fields = ['object', 'photo']
