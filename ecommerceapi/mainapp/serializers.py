from rest_framework import serializers

from mainapp.models import *


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

