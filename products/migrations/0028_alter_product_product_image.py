# Generated by Django 4.2.7 on 2023-12-19 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='products/product_cover/', verbose_name='Product Image'),
        ),
    ]
