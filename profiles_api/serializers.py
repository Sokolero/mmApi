from rest_framework import serializers

from api.models import Object, Category, Gallery
from users.models import CustomUser

class ObjectSerializer(serializers.ModelSerializer):
    X = serializers.CharField(max_length=10)
    Y = serializers.CharField(max_length=10)
    date_of_creation = serializers.DateTimeField(read_only=True)
    categorys = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True
    )

    class Meta:
        model = Object
        fields = ('id', 'user', 'X', 'Y', 'date_of_creation', 'categorys')

class GallerySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    object = serializers.PrimaryKeyRelatedField(queryset=Object.objects.all())
    photo = serializers.ImageField()

    class Meta:
        model = Gallery
        fields = ('id', 'user', 'object', 'photo')
