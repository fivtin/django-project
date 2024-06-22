from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def get_category_list():
    if CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list:
            return category_list
        category_list = Category.objects.all()
        cache.set(key, category_list)
        return category_list
    else:
        return Category.objects.all()


def get_product_list():
    if CACHE_ENABLED:
        key = 'product_list'
        product_list = cache.get(key)
        if product_list:
            return product_list
        product_list = Product.objects.all()
        cache.set(key, product_list)
        return product_list
    else:
        return Product.objects.all()
