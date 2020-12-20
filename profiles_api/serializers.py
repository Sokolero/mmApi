from rest_framework import serializers
from api.models import Object, Category, Gallery
from users.models import CustomUser



# GallerySerializer
class GallerySerializer(serializers.HyperlinkedModelSerializer):
    object = serializers.ReadOnlyField(source='object')
    photo = serializers.ImageField()

    class Meta:
        model = Gallery
        fields = ('url', 'id', 'object', 'photo')

#------------------------------------------------------------------------------
class GalleryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ('object', 'photo')
        read_only_fields = ['object', 'photo']


#-------------------------------------------------------------------------------
class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    X = serializers.CharField(max_length=10)
    Y = serializers.CharField(max_length=10)
    categorys = serializers.ListField(child=serializers.CharField())
    files = serializers.ListField(child=serializers.ImageField(), write_only=True)




class ObjectListSerializer(serializers.HyperlinkedModelSerializer):
        X = serializers.CharField(max_length=10)
        Y = serializers.CharField(max_length=10)
        categorys = serializers.PrimaryKeyRelatedField(queryset=Object.objects.all(), many=True)
        gallerys = serializers.HyperlinkedRelatedField(queryset=Gallery.objects.all(), many=True, view_name='gallery-list')

        class Meta:
            model = Object
            fields = ('url', 'id', 'X', 'Y', 'categorys', 'gallerys')
