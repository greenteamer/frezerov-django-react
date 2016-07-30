# coding: utf8
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class Category(models.Model):
  parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
  name = models.CharField(max_length=100, verbose_name=u'Название категории')
  slug = models.SlugField(max_length=50, unique=True)

  def __unicode__(self):
    return self.name


class AttributeType(models.Model):
  name = models.CharField(max_length=100, verbose_name=u'Название атрибута')
  slug = models.SlugField(max_length=50, unique=True)

  def __unicode__(self):
    return self.name


class AttributeValue(models.Model):
  attributeType = models.ForeignKey(AttributeType, related_name="attribute_type__value")
  value = models.CharField(max_length=100, verbose_name=u'Значение атрибута')

  def __unicode__(self):
    return "{0} - {1}".format(self.attributeType, self.value)


class Product(models.Model):
  category = models.ForeignKey(Category, related_name="category__products")
  name = models.CharField(max_length=100, verbose_name=u'Название продукта')
  slug = models.SlugField(max_length=50, unique=True)
  description = RichTextField(verbose_name=u'дополнительное описание продукта')
  price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u'цена')

  def __unicode__(self):
    return self.name


class ProductParam(models.Model):
  product = models.ForeignKey(Product, related_name="product__params")
  attributeType = models.ForeignKey(AttributeType, related_name="product_param__attribute_type")
  attributeValues = models.ManyToManyField(AttributeValue)

  def __unicode__(self):
    return "{0} - {1}".format(self.product, self.attributeType)
