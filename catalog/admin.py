from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    search_fields = ('title', 'description', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', )
    list_filter = ('category__title', )
    search_fields = ('title', 'description', )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'title', 'product', 'is_current', )
    list_filter = ('product__title', 'is_current', )
    search_fields = ('is_current', 'product', )
