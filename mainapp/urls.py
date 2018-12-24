from django.urls import path
from .views import main_view, projects_view, contacts_view, products_of_categories_view

app_name = 'mainapp'

urlpatterns = [
    path('', main_view, name='main'),
    path('projects/', projects_view, name='projects'),
    path('contacts/', contacts_view, name='contacts'),
    path('projects/<pk>/', products_of_categories_view, name='products_of_categories'),
]


