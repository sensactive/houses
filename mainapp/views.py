from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from basketapp.models import Basket
import random

def get_categories():
    return Category.objects.all().exclude(is_active=False)

# Create your views here.
def main_view(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    products = Product.objects.filter(is_active=True)
    products = random.sample(list(products), 6)
    len_items = len(get_categories())
    content = {
        'categories': get_categories(),
        'len_items': len_items,
        'basket': basket,
        'products': products
    }
    return render(request, 'mainapp/index.html',  content)

def projects_view(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    len_items = len(get_categories())
    content = {
        'categories': get_categories(),
        'len_items': len_items,
        'basket': basket
    }
    return render(request, 'mainapp/projects.html', content)

def contacts_view(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        'basket': basket,
        'categories': get_categories()
    }
    return render(request, 'mainapp/contacts.html', content)

def products_of_categories_view(request, pk, page=1):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk == 0:
        products = Product.objects.filter(is_active=True, category__is_active=True)
        category = {'name': 'All', 'pk': '0'}
    else:
        category = Category.objects.get(pk=pk)
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
        'basket': basket,
        'categories': get_categories()
    }
    return render(request, 'mainapp/products.html', content)

def product(request, pk):
    one_product = get_object_or_404(Product, pk=pk)
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        'categories': get_categories(),
        'product': one_product,
        'basket': basket
    }
    return render(request, 'mainapp/product.html', content)