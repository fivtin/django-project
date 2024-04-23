from django.urls import path

from catalog.views import home_page, contacts_page

# app_name = 'students_list'

urlpatterns = [
    path('', home_page),
    path('contacts/', contacts_page),
]
