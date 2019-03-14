from basketapp.models import Basket
from .models import Category
from .views import get_links_menu

def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return {
        'basket': basket
    }

# получение категорий для выпадающего меню OUR HOUSES
def get_categories(request):
    # categories = Category.objects.all().exclude(is_active=False)
    categories = get_links_menu() # кэшируем категории

    return {
        'categories': categories
    }