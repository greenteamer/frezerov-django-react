# coding: utf8
from django.contrib.auth.models import User
from rest_framework import viewsets
from core.api.serializers import *
from core.models import *


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class ProductParamViewSet(viewsets.ModelViewSet):
  queryset = ProductParam.objects.all()
  serializer_class = ProductParamSerializer


class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  view_name='category'
