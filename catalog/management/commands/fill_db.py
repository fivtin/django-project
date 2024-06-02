import json
import os.path

from django.core.management import BaseCommand

from blog.models import Blog
from catalog.models import Product, Category
from config.settings import BASE_DIR


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(os.path.join(BASE_DIR, 'fixtures', 'categories.json'), encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def json_read_products():
        with open(os.path.join(BASE_DIR, 'fixtures', 'products.json'), encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def json_read_blogs():
        with open(os.path.join(BASE_DIR, 'fixtures', 'blogs.json'), encoding='utf-8') as f:
            return json.load(f)

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Blog.objects.all().delete()

        product_for_create = []
        category_for_create = []
        blog_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(**category)
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                # Product(название_поля=значение_из_словаря, ...,
                #                                 # получаем категорию из базы данных для корректной связки объектов
                #         поле_категории=Category.objects.get(pk=значение_из_словаря), ...,
                #         название_поля=значение_из_словаря)
                Product(**product)
            )

        Product.objects.bulk_create(product_for_create)

        for blog in Command.json_read_blogs():
            blog_for_create.append(
                Blog(**blog)
            )

        Blog.objects.bulk_create(blog_for_create)
