from django.db import models


NULLABLE = {
    'null': True,
    'blank': True,
}


class Category(models.Model):
    """ A class that implements the 'category' model. """

    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'<Category: {self.title}>'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """ A class that implements the 'product' model. """

    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Product: {self.title}, price: {self.price}>'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
