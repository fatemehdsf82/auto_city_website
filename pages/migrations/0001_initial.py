# Generated by Django 4.2.7 on 2023-12-27 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, verbose_name=datetime.datetime.now)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
