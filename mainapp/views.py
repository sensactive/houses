from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
import random


# Create your views here.
def main_view(request):
    products = Product.objects.filter(is_active=True)
    products = random.sample(list(products), 6)
    content = {
        'products': products
    }
    return render(request, 'mainapp/index.html',  content)

def projects_view(request):
    return render(request, 'mainapp/projects.html')

def contacts_view(request):
    return render(request, 'mainapp/contacts.html')

def products_of_categories_view(request, pk, page=1):
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
    }
    return render(request, 'mainapp/products.html', content)

def product(request, pk):
    one_product = get_object_or_404(Product, pk=pk)
    content = {
        'product': one_product
    }
    return render(request, 'mainapp/product.html', content)