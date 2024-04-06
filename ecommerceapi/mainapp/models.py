from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.TextField(null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class ProductCart(models.Model):
    product = models.ManyToManyField(Products, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Product Cart"



