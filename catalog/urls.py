from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import main_page, contacts, product_detail


app_name = CatalogConfig.name # 'catalog'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts'),
]
