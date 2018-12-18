from django.shortcuts import render
from .models import Category, Product
from basketapp.models import Basket

# Create your views here.
def main_view(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    typesItem = Category.objects.all()
    len_items = len(typesItem)
    return render(request, 'mainapp/index.html',  {'typeItems': typesItem, 'len_items': len_items, 'basket': basket})

def projects_view(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    typesItem = Category.objects.all()
    len_items = len(typesItem)
    return render(request, 'mainapp/projects.html', {'items': typesItem, 'len_items': len_items, 'basket': basket})

def contacts_view(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    return render(request, 'mainapp/contacts.html', {'basket': basket})

def products_of_categories_view(request, pk):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'mainapp/products.html', {'products': products, 'category': category, 'basket': basket})