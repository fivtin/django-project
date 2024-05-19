from django.db import models

NULLABLE = {
    'null': True,
    'blank': True,
}


class Blog(models.Model):
    """ A class that implements the 'blog' model. """

    title = models.CharField(max_length=128, verbose_name='заголовок')
    slug = models.CharField(max_length=150)
    content = models.TextField( verbose_name='содержимое')
    preview = models.ImageField(upload_to='images/blog/', **NULLABLE,  verbose_name='превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('id', )
