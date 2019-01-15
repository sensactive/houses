from django.urls import path
from .views import main_view, projects_view, contacts_view, products_of_categories_view, product

app_name = 'mainapp'

urlpatterns = [
    path('', main_view, name='main'),
    path('projects/', projects_view, name='projects'),
    path('contacts/', contacts_view, name='contacts'),
    path('projects/<int:pk>/page/<int:page>', products_of_categories_view, name='page'),
    path('product/<pk>/', product, name='product'),
]


