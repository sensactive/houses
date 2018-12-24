from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import Product
from .models import Basket

# Create your views here.

def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    basket_items = Basket.objects.filter(user=request.user). \
        order_by('product__category')

    content = {
        'basket_items': basket_items,
        'basket': basket
    }

    return render(request, 'basket.html', content)


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


def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))