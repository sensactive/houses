from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def main_view(request):
    typesItem = Category.objects.all()
    len_items = len(typesItem)
    return render(request, 'mainapp/index.html',  {'typeItems': typesItem, 'len_items': len_items})

def projects_view(request):
    typesItem = Category.objects.all()
    len_items = len(typesItem)
    return render(request, 'mainapp/projects.html', {'items': typesItem, 'len_items': len_items})

def contacts_view(request):
    return render(request, 'mainapp/contacts.html')

def products_view(request):
    category = Category.objects.first()
    products = Product.objects.all()
    return render(request, 'mainapp/product.html', {'products': products, 'qw': category})