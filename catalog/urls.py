from django.urls import path

from catalog.views import main_page, contacts, product_detail

# app_name = 'students_list'

urlpatterns = [
    path('', main_page),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('contacts/', contacts),
]
