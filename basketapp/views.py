from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from .models import Basket

# Create your views here.

def basket(request):
    content = {}
    return render(request, 'mainapp/products.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    old_basket_item = Basket.objects.filter(user=request.user, product=product)
    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket(user=request.user, product=product)
        new_basket_item.quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)