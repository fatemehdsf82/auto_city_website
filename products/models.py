from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("ghataat_badaneh", "بدنه"),
        ("motor_exoz", "موتور_اگزوز"),
        ("barghi_electricy", "برقی_الکتریکی"),
        ("roghan_filter", "روغن_فیلتر"),
        ("ghataat_dakheli", "قطعات داخلی"),
        ("enteghal_ghodrat", "انتقال قدرت"),
        ("farman_jelobandi_tormoz", "فرمان_جلوبندی_ترمز"),
        ("bolboring", "بولبورینگ"),
        ("kasenamad", "کاسه نمد"),
        ("oring", "اورینگ"),
        ("gardgir", "گردگیر"),
        ("looleh", "لوله"),
        ("tasmeh", "تسمه"),
        ("shelang", "شلنگ"),
    ]

    BRAND_CHOICES = [
        ("saipa", "سایپا"),
        ("mashad_washer", "مشهد واشر"),
        ("HIC", "اچ آی سی"),
        ("ezaam", "عظام"),
        ("crouse", "کروز"),
        ("amirnia", "امیرنیا"),
        ("jahan_lent", "جهان لنت"),
        ("behran", "بهران"),
        ("isaco", "ایساکو"),
    ]
    product_id = models.AutoField(primary_key=True, name="id")
    product_name = models.CharField(max_length=100, name="name")

    #! description added
    product_description = models.TextField(null=True, name="description")
    product_cost = models.PositiveIntegerField(name="cost")
    product_category = models.CharField(
        max_length=40, choices=CATEGORY_CHOICES, name="category"
    )
    product_brand = models.CharField(
        max_length=40, choices=BRAND_CHOICES, default="blank", name="brand"
    )

    # product_image = models.ImageField(
    #     verbose_name=("Product Image"),
    #     upload_to="products/product_images/",
    #     blank=True,
    # )

    product_stock = models.IntegerField(default=0, name="stock")

    product_status = models.BooleanField(default=True, name="status")

    # product_created_at = models.DateTimeField(datetime.now, name="created_at")
    # product_updated_at = models.DateTimeField(
    #     auto_now=True, null=True, name="modified_at"
    # )

    datetime_created = models.DateTimeField(auto_now_add=True, name="created_at")
    datetime_modified = models.DateTimeField(auto_now=True, name="modified_at")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])


class Comment(models.Model):
    PRODUCT_STARS = [
        ("1", "Very Bad"),
        ("2", "Bad"),
        ("3", "Normal"),
        ("4", "Good"),
        ("5", "Very Good"),
    ]

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="comments",
        name="author",
    )
    body = models.TextField(verbose_name=_("comment_text"), name="text")
    # comment_created_at = models.DateTimeField(datetime.now, name="created_at")
    # comment_updated_at = models.DateTimeField(
    #     auto_now=True, null=True, name="modified_at"
    # )
    datetime_created = models.DateTimeField(auto_now_add=True, name="created_at")
    datetime_modified = models.DateTimeField(auto_now=True, name="modified_at")

    star = models.CharField(
        max_length=10,
        choices=PRODUCT_STARS,
        name="star",
        default=5,
        verbose_name=_("score"),
    )
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product_id])
