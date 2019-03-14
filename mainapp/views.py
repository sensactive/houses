from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
import random

from django.conf import settings
from django.core.cache import cache

from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from django.http import JsonResponse



def get_links_menu():
   if settings.LOW_CACHE:
       key = 'links_menu'
       links_menu = cache.get(key)
       if links_menu is None:
           links_menu = Category.objects.filter(is_active=True)
           cache.set(key, links_menu)
       return links_menu
   else:
       return Category.objects.filter(is_active=True)


def get_category(pk):
   if settings.LOW_CACHE:
       key = 'category_{}'.format(pk)
       category = cache.get(key)
       if category is None:
           category = get_object_or_404(Category, pk=pk)
           cache.set(key, category)
       return category
   else:
       return get_object_or_404(Category, pk=pk)


def get_products():
   if settings.LOW_CACHE:
       key = 'products'
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product(pk):
   if settings.LOW_CACHE:
       key = 'product_{}'.format(pk)
       product = cache.get(key)
       if product is None:
           product = get_object_or_404(Product, pk=pk)
           cache.set(key, product)
       return product
   else:
       return get_object_or_404(Product, pk=pk)


# def get_products_orederd_by_price():
#    if settings.LOW_CACHE:
#        key = 'products_orederd_by_price'
#        products = cache.get(key)
#        if products is None:
#            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
#            cache.set(key, products)
#        return products
#    else:
#        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
   if settings.LOW_CACHE:
       key = 'products_in_category_orederd_by_price_{}'.format(pk)
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')

# Create your views here.
def main_view(request):
    products = Product.objects.filter(is_active=True)
    if products:
        products = random.sample(list(products), 6)
    content = {
        'products': products
    }
    return render(request, 'mainapp/index.html',  content)

def projects_view(request):
    return render(request, 'mainapp/projects.html')

def contacts_view(request):
    return render(request, 'mainapp/contacts.html')


def products_ajax(request, pk=None, page=1):
   if request.is_ajax():
       if pk:
           if pk == '0':
               products = get_products()  # кэшируем продукты
               category = {'name': 'All', 'pk': '0'}
           else:
               category = get_category(pk)
               products = get_products_in_category_orederd_by_price(pk)

           paginator = Paginator(products, 2)
           try:
               products_paginator = paginator.page(page)
           except PageNotAnInteger:
               products_paginator = paginator.page(1)
           except EmptyPage:
               products_paginator = paginator.page(paginator.num_pages)

           content = {
               'category': category,
               'products': products_paginator,
           }

           result = render_to_string('mainapp/include/inc_products.html', context=content, request=request)

           return JsonResponse({'result': result})


def products_of_categories_view(request, pk, page=1):
    if pk == 0:
        # products = Product.objects.filter(is_active=True, category__is_active=True)
        products = get_products() # кэшируем продукты
        category = {'name': 'All', 'pk': '0'}
    else:
        # category = Category.objects.get(pk=pk)
        category = get_category(pk) # кэшируем категорию
        products = Product.objects.filter(category=category, is_active=True, category__is_active=True)
    paginator = Paginator(products, 2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    content = {
        'products': products_paginator,
        'category': category,
    }
    return render(request, 'mainapp/products.html', content)

def product(request, pk):
    # one_product = get_object_or_404(Product, pk=pk)
    one_product = get_product(pk) # кэшируем продукт
    content = {
        'product': one_product
    }
    return render(request, 'mainapp/product.html', content)
