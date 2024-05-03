from django.db import models


class Product(models.Model):
    """ A class that implements the 'product' model. """

    def __str__(self):
        return '<Product: >'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    """ A class that implements the 'category' model. """

    def __str__(self):
        return '<Category: >'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

