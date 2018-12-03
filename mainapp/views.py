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

def products_of_categories_view(request, pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'mainapp/product.html', {'products': products, 'category': category})