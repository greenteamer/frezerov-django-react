# coding: utf8
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from core.models import Product
# for react ssr
import json
from react.render import render_component
import os

def home(request, template_name="core/home.html"):
  return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def home(request, template_name='core/home.html'):

  products = Product.objects.all()
  # # new_test = STATIC_ROOT
  # slides = Slide.objects.all()

  # for product in products:
  #   product.list_parametr = ProductParametr.objects.filter(product=product)

  # if request.method == 'POST':
  #   add_to_cart(request)

  # articles = Article.objects.all()
  # for art in articles:
  #   try:
  #     art.image = ArticleImage.objects.filter(article=art)[0]
  #   except:
  #     pass

  # pages = Page.objects.all()
  # for pag in pages:
  #   try:
  #     pag.image = PageImage.objects.filter(page=pag)
  #     pag.image = pag.image[0]
  #   except:
  #     pass

  # REACT server side render
  prod_arr = []
  for product in products:
    prod_arr.append(
      {
        "id": product.id,
        "name": product.name,
        "slug": product.slug,
        "description": product.description,
        # "weight": product.weight,
        # "price": product.price,
        # "product_images": product.get_image().get_image_url()
      }
    )

  rendered = render_component(
    os.path.join(os.getcwd(), 'project', 'static', 'app', 'src', 'App', 'App.js'),
    {
      'is_server': [],
      'products': prod_arr
    },
    to_static_markup=True,
  )

  return render_to_response(template_name, locals(), context_instance=RequestContext(request))
  # return render(request, 'core/index.html', {'products': products ,'articles' : articles })
