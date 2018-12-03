from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import main_view, projects_view, contacts_view, products_of_categories_view

urlpatterns = [
    path('', main_view, name='main'),
    path('projects/', projects_view, name='projects'),
    path('contacts/', contacts_view, name='contacts'),
    path('projects/<pk>', products_of_categories_view, name='products_of_categories')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

