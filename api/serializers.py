from rest_framework import serializers
from .models import Object, Category, Master, Category
from users.models import CustomUser
from django.shortcuts import get_object_or_404



class ObjectListSerializer(serializers.ModelSerializer):
    X = serializers.CharField(max_length=10)
    Y = serializers.CharField(max_length=10)
    master = serializers.PrimaryKeyRelatedField(read_only=True)
    date_of_creation = serializers.DateTimeField()
    categorys = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Object
        fields = '__all__'


class ObjectSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    X = serializers.CharField(max_length=10)
    Y = serializers.CharField(max_length=10)
    date_of_creation = serializers.DateTimeField()
    categorys = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all()
    )

    class Meta:
        model = Object
        fields = '__all__'


class MasterSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    categorys = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True
    )

    class Meta:
        model = Master
        fields = ['user','first_name', 'last_name', 'phone', 'categorys']

    def create(self, validated_data):
        master = Master.objects.create(
            user=validated_data['user'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone = validated_data['phone']
        )
        master.categorys.set(validated_data['categorys'])
        user = CustomUser.objects.get(pk=validated_data['user'])
        user.is_master = True
        user.save()
        master.save()
        print(user.is_master)
        print(user.id)
        return master


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = '__all__'
