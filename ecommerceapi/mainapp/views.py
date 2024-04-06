from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .models import *
from .serializers import ProductSerializer, ProductCartSerializer, UserSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class ProductCartViewSet(viewsets.ModelViewSet):
    queryset = ProductCart.objects.all()
    serializer_class = ProductCartSerializer
    permission_classes = (IsAuthenticated,)


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
