from rest_framework import serializers
from .models import CustomUser
from api.models import Category

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def create(self, validated_data):
        user = CustomUser(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class CreateMasterSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length=128)
    last_name = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=32)
    categorys = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'categorys')
