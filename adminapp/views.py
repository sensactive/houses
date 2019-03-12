from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from mainapp.models import Product, Category
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import ShopUserAdminEditForm, CategoryAdminEditForm, ProductAdminEditForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     content = {
#         'categories': get_categories(),
#         'objects': users_list,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/users.html', content)

class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    paginate_by = 5

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = get_categories()   // эта часть вынесена в контекстный процессор в mainapp

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('adminapp:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     content = {
#         'categories': get_categories(),
#         'update_form': user_form,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/user_update.html', content)


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:users')



    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_user)
#
#     content = {
#         'categories': get_categories(),
#         'update_form': edit_form,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/user_update.html', content)


class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('adminapp:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         # user.delete()
#         # вместо удаления лучше сделаем неактивным
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('adminapp:users'))
#
#     content = {
#         'categories': get_categories(),
#         'user_to_delete': user,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/user_delete.html', content)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('adminapp:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     categories_list = Category.objects.all()
#     content = {
#         'categories': get_categories(),
#         'objects': categories_list,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/categories.html', content)


class CategoryListView(ListView):
    model = Category
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context





# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     if request.method == 'POST':
#         category_form = CategoryAdminEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('adminapp:categories'))
#     else:
#         category_form = CategoryAdminEditForm()
#
#     content = {
#         'categories': get_categories(),
#         'update_form': category_form,
#         'basket': basket
#     }
#     return render(request, 'adminapp/category_update.html', content)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryAdminEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     edit_category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         edit_form = CategoryAdminEditForm(request.POST, request.FILES, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = CategoryAdminEditForm(instance=edit_category)
#
#     content = {
#         'categories': get_categories(),
#         'update_form': edit_form,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/category_update.html', content)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryAdminEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('adminapp:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     category = get_object_or_404(Category, pk=pk)
#
#     if request.method == 'POST':
#         # user.delete()
#         # вместо удаления лучше сделаем неактивным
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('adminapp:categories'))
#
#     content = {
#         'categories': get_categories(),
#         'category_to_delete': category,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/category_delete.html', content)


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('adminapp:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def products(request):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     products_list = Product.objects.all().order_by('category__name')
#
#     content = {
#         'categories': get_categories(),
#         'objects': products_list,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/products.html', content)


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'
    paginate_by = 5

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     if request.method == 'POST':
#         product_form = ProductAdminEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('adminapp:products'))
#     else:
#         product_form = ProductAdminEditForm()
#
#     content = {
#         'categories': get_categories(),
#         'update_form': product_form,
#         'basket': basket
#     }
#     return render(request, 'adminapp/product_update.html', content)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductAdminEditForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('adminapp:product')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     edit_product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductAdminEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:product_update', args=[edit_product.pk]))
#     else:
#         edit_form = CategoryAdminEditForm(instance=edit_product)
#
#     content = {
#         'categories': get_categories(),
#         'update_form': edit_form,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/product_update.html', content)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductAdminEditForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('adminapp:products')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         # user.delete()
#         # вместо удаления лучше сделаем неактивным
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('adminapp:products'))
#
#     content = {
#         'categories': get_categories(),
#         'product_to_delete': product,
#         'basket': basket
#     }
#
#     return render(request, 'adminapp/product_delete.html', content)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('adminapp:products')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

