from django.urls import path

import basketapp.views as basketapp

app_name='basketapp'

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<pk>/', basketapp.basket_add, name='add'),
    path('remove/<pk>/', basketapp.basket_remove, name='remove'),
]