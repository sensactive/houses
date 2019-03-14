from django.urls import path
from .views import main_view, projects_view, contacts_view, products_of_categories_view, product, products_ajax
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    path('', main_view, name='main'),
    path('projects/', projects_view, name='projects'),
    path('projects/<int:pk>/page/<int:page>/ajax/', cache_page(3600)(products_ajax)),
    path('contacts/', contacts_view, name='contacts'),
    path('projects/<int:pk>/page/<int:page>/', products_of_categories_view, name='page'),
    path('product/<pk>/', product, name='product'),
]


