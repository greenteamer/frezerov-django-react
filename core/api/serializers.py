# coding: utf8
from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import *
from core.api.flatserializers import *


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email', 'is_staff')


class ProductParamSerializer(serializers.ModelSerializer):
  attributeType = AttributeTypeObj(read_only=True)
  attributeValues = AttributeValueObj(many=True, read_only=True)
  class Meta:
    model = ProductParam
    fields = ('url', 'id', 'product', 'attributeType', 'attributeValues' )


class ProductSerializer(serializers.ModelSerializer):
  product__params = ProductParamSerializer(many=True, read_only=True)
  category = CategoryObj(read_only=True)
  class Meta:
    model = Product
    fields = ('url', 'id', 'category', 'name', 'slug', 'description', 'price', 'product__params')


class CategorySerializer(serializers.ModelSerializer):
  category__products = ProductSerializer(many=True, read_only=True)
  class Meta:
    model = Category
    fields = ('url', 'id', 'name', 'slug', 'category__products')
