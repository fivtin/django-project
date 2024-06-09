from django.db import models

from config import NULLABLE
from users.models import User


class Category(models.Model):
    """ A class that implements the 'category' model. """

    title = models.CharField(max_length=128, verbose_name='категория')
    description = models.TextField( verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('id', )


class Product(models.Model):
    """ A class that implements the 'product' model. """

    title = models.CharField(max_length=128, verbose_name='продукт')
    description = models.TextField( verbose_name='описание')
    image = models.ImageField(upload_to='images/', **NULLABLE,  verbose_name='превью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='дата добавления')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='дата изменения')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='кто добавил', **NULLABLE)

    def __str__(self):
        return f'{self.title}, цена: {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('id', )


class Version(models.Model):
    """ A class that implements the 'version' model. """

    product = models.ForeignKey(Product, on_delete=models.CASCADE,  verbose_name='продукт')
    number = models.CharField(max_length=32, verbose_name='номер версии')
    title = models.CharField(max_length=128, verbose_name='название версии')
    is_current = models.BooleanField(default=False, verbose_name='текущая')
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='дата добавления')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='дата изменения')

    def __str__(self):
        return f'{self.number}: {self.title}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('product', 'is_current', 'number', )
