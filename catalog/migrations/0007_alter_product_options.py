# Generated by Django 4.2 on 2024-06-16 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_product_options_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',), 'permissions': [('set_published', 'Can publish product'), ('set_category', 'Can change category'), ('set_description', 'Can change description')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]