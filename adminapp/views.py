from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from mainapp.models import Product, Category
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import ShopUserAdminEditForm, CategoryAdminEditForm
from basketapp.models import Basket
from mainapp.views import get_categories

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'categories': get_categories(),
        'objects': users_list,
        'basket': basket
    }

    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {
        'categories': get_categories(),
        'update_form': user_form,
        'basket': basket
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {
        'categories': get_categories(),
        'update_form': edit_form,
        'basket': basket
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('adminapp:users'))

    content = {
        'categories': get_categories(),
        'user_to_delete': user,
        'basket': basket
    }

    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    categories_list = Category.objects.all()
    content = {
        'categories': get_categories(),
        'objects': categories_list,
        'basket': basket
    }

    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if request.method == 'POST':
        category_form = CategoryAdminEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        category_form = CategoryAdminEditForm()

    content = {
        'categories': get_categories(),
        'update_form': category_form,
        'basket': basket
    }
    return render(request, 'adminapp/category_update.html', content)



@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    edit_category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        edit_form = CategoryAdminEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:category_update', args=[edit_category.pk]))
    else:
        edit_form = CategoryAdminEditForm(instance=edit_category)

    content = {
        'categories': get_categories(),
        'update_form': edit_form,
        'basket': basket
    }

    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    content = {
        'categories': get_categories(),
        'category_to_delete': category,
        'basket': basket
    }

    return render(request, 'adminapp/category_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    category = get_object_or_404(Category, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'categories': get_categories(),
        'category': category,
        'objects': products_list,
        'basket': basket
    }

    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    pass
