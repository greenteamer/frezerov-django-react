# coding: utf8
from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import *


class CategoryObj(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('url', 'id', 'name', 'slug', 'parent')


class AttributeTypeObj(serializers.ModelSerializer):
  class Meta:
    model = AttributeType


class AttributeValueObj(serializers.ModelSerializer):
  class Meta:
    model = AttributeValue


class ProductParamObj(serializers.ModelSerializer):
  class Meta:
    model = ProductParam


class ProductObj(serializers.ModelSerializer):
  category = CategoryObj(read_only=True)
  product__params = ProductParamObj(many=True, read_only=True)
  class Meta:
    model = Product
    fields = ('url', 'id', 'category', 'name', 'slug', 'description', 'price', 'product__params')
