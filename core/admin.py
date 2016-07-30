# coding: utf8
from django.contrib import admin
from django import forms
from models import Product, Category, AttributeType, AttributeValue, ProductParam


class CategoryAdmin(admin.ModelAdmin):
  model = Category
  prepopulated_fields = {'slug': ('name', ), }

class AttributeValueInline(admin.StackedInline):
  model = AttributeValue
  extra = 1

class AttributeAdmin(admin.ModelAdmin):
  model = AttributeType
  prepopulated_fields = {'slug': ('name', ), }
  inlines = [ AttributeValueInline, ]

class ProductParamInline(admin.StackedInline):
  model = ProductParam
  filter_horizontal = ('attributeValues', )
  extra = 0

class ProductAdmin(admin.ModelAdmin):
  model = Product
  prepopulated_fields = {'slug': ('name', ), }
  inlines = [ ProductParamInline, ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(AttributeType, AttributeAdmin)
