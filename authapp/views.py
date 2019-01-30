from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse
from basketapp.models import Basket
from mainapp.models import Category
from django.core.mail import send_mail
from django.conf import settings
from authapp.models import ShopUser


categories = Category.objects.all()

def login(request):

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST':

        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('mainapp:main'))
    else:
        login_form = ShopUserLoginForm()

    content = {
        'login_form': login_form,
        'categories': categories,
        'next': next
    }

    return render(request, 'login.html', content)

def login_after_registration(request):
    return render(request, 'login_a_r.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:main'))


def register(request):

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('authapp:login_a_r'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {
        'register_form': register_form,
        'categories': categories
    }

    return render(request, 'register.html', content)


def edit(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {
        'edit_form': edit_form,
        'basket': basket,
        'categories': categories
    }

    return render(request, 'edit.html', content)


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.pk, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на портале \
{settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, pk, activation_key):
    try:
        user = ShopUser.objects.get(pk=pk)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('authapp:login'))