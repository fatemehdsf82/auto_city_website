# Generated by Django 4.2.7 on 2023-12-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='pages/post_cover/', verbose_name='تصویر پست'),
        ),
    ]