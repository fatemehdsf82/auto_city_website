# Generated by Django 4.2.7 on 2023-12-01 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_product_description_product_product_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_updated_at',
            new_name='modified_at',
        ),
    ]
