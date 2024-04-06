from rest_framework import serializers
from mainapp.models import *
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Products
        fields = '__all__'


class ProductCartSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True)
    class Meta:
        model = ProductCart
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
