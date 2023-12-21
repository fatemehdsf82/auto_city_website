# Generated by Django 4.2.7 on 2023-12-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ghataat_badaneh', 'بدنه'), ('motor_exoz', 'موتور_اگزوز'), ('barghi_electricy', 'برقی_الکتریکی'), ('roghan_filter', 'روغن_فیلتر'), ('ghataat_dakheli', 'قطعات داخلی'), ('enteghal_ghodrat', 'انتقال قدرت'), ('farman_jelobandi_tormoz', 'فرمان_جلوبندی_ترمز'), ('bolboring', 'بولبرینگ'), ('kasenamad', 'کاسه نمد'), ('oring', 'اورینگ'), ('gardgir', 'گردگیر'), ('looleh', 'لوله'), ('tasmeh', 'تسمه'), ('shelang', 'شلنگ')], max_length=40),
        ),
    ]
