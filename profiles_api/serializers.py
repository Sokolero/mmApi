from rest_framework import serializers
from api.models import Object, Category, Gallery
from users.models import CustomUser

CHOICES = ('Бетонные работы', 'Электрика', 'Кровельные работы', 'Отделочные работы')

class CategoryListField(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

#---------------------
class GallerySerializer(serializers.HyperlinkedModelSerializer):
    object = serializers.ReadOnlyField(source='object.id')

    class Meta:
        model = Gallery
        fields = ['url', 'id', 'object', 'photo']

#new
class ObjectSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    # gallerys = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='gallery-detail')
    gallerys = GallerySerializer(many=True, read_only=True)
    categorys = CategoryListField(many=True, read_only=True)
    selected_categorys = serializers.ListField(child=serializers.CharField(), write_only=True)
    files = serializers.ListField(child=serializers.ImageField(), write_only=True)

    class Meta:
        model = Object
        fields = ['url', 'id', 'X', 'Y', 'user', 'categorys', 'selected_categorys', 'gallerys', 'files']

# # GallerySerializer
# class GallerySerializer(serializers.HyperlinkedModelSerializer):
#     object = serializers.ReadOnlyField(source='object')
#     photo = serializers.ImageField()
#
#     class Meta:
#         model = Gallery
#         fields = ('url', 'id', 'object', 'photo')
#
# #------------------------------------------------------------------------------
# class GalleryDetailSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Gallery
#         fields = ('object', 'photo')
#         read_only_fields = ['object', 'photo']
#
#
# #-------------------------------------------------------------------------------
# class ObjectSerializer(serializers.HyperlinkedModelSerializer):
#     X = serializers.CharField(max_length=10)
#     Y = serializers.CharField(max_length=10)
#     categorys = serializers.ListField(child=serializers.CharField())
#     files = serializers.ListField(child=serializers.ImageField(), write_only=True)
#
#
#
#
# class ObjectListSerializer(serializers.HyperlinkedModelSerializer):
#         X = serializers.CharField(max_length=10)
#         Y = serializers.CharField(max_length=10)
#         categorys = serializers.PrimaryKeyRelatedField(queryset=Object.objects.all(), many=True)
#         gallerys = serializers.HyperlinkedRelatedField(queryset=Gallery.objects.all(), many=True, view_name='gallery-list')
#
#         class Meta:
#             model = Object
#             fields = ('url', 'id', 'X', 'Y', 'categorys', 'gallerys')
