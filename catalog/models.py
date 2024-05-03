from django.db import models


NULLABLE = {
    'null': True,
    'blank': True,
}


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

    def __str__(self):
        return f'{self.title}, цена: {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('id', )
