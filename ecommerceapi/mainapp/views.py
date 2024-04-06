from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import *
from .serializers import ProductSerializer, ProductCartSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class ProductCartViewSet(viewsets.ModelViewSet):
    queryset = ProductCart.objects.all()
    serializer_class = ProductCartSerializer
    permission_classes = (IsAuthenticated,)
