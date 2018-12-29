from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from basketapp.models import Basket

def get_categories():
    return Category.objects.all().exclude(is_active=False)

# Create your views here.
def main_view(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    len_items = len(get_categories())
    content = {
        'categories': get_categories(),
        'len_items': len_items,
        'basket': basket,
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

def products_of_categories_view(request, pk):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk == '0':
        products = Product.objects.all()
        category = {'name': 'All'}
    else:
        category = Category.objects.get(pk=pk)
        products = Product.objects.filter(category=category)
    content = {
        'products': products,
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