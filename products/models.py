from email.policy import default
from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from sqlalchemy import null, true


class Product(models.Model):
    # CATEGORY_CHOICES = [
    #     ("ghataat_badaneh", "بدنه"),
    #     ("motor_exoz", "موتور_اگزوز"),
    #     ("barghi_electricy", "برقی_الکتریکی"),
    #     ("roghan_filter", "روغن_فیلتر"),
    #     ("ghataat_dakheli", "قطعات داخلی"),
    #     ("enteghal_ghodrat", "انتقال قدرت"),
    #     ("farman_jelobandi_tormoz", "فرمان_جلوبندی_ترمز"),
    #     ("bolboring", "بولبرینگ"),
    #     ("kasenamad", "کاسه نمد"),
    #     ("oring", "اورینگ"),
    #     ("gardgir", "گردگیر"),
    #     ("looleh", "لوله"),
    #     ("tasmeh", "تسمه"),
    #     ("shelang", "شلنگ"),
    # ]

    # BRAND_CHOICES = [
    #     ("saipa", "سایپا"),
    #     ("mashad_washer", "مشهد واشر"),
    #     ("HIC", "اچ آی سی"),
    #     ("ezaam", "عظام"),
    #     ("crouse", "کروز"),
    #     ("amirnia", "امیرنیا"),
    #     ("jahan_lent", "جهان لنت"),
    #     ("behran", "بهران"),
    #     ("isaco", "ایساکو"),
    # ]
    product_id = models.AutoField(primary_key=True, name="id")
    product_name = models.CharField(max_length=100, name="name")
    product_car_type = models.CharField(max_length=100, name="car_type", null=True)
    product_description = models.TextField(null=True, name="description", blank=True)
    product_price = models.PositiveIntegerField(name="price")
    product_category = models.CharField(max_length=40, name="category")
    product_brand = models.CharField(max_length=40, null=True, name="brand")

    product_image = models.ImageField(
        verbose_name=_("Product Image"),
        upload_to="products/product_cover/",
        blank=True,
        name="image",
    )

    product_stock = models.IntegerField(default=0, name="stock", blank=True)

    product_status = models.BooleanField(default=True, name="status", blank=True)

    product_created_at = models.DateTimeField(
        datetime.now, name="created_at", blank=True
    )
    product_updated_at = models.DateTimeField(
        auto_now=True, null=True, name="modified_at", blank=True
    )

    # datetime_created = models.DateTimeField(auto_now_add=True, name="created_at")
    # datetime_modified = models.DateTimeField(auto_now=True, name="modified_at")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])


class Comment(models.Model):
    PRODUCT_STARS = [
        ("1", _("Very Bad")),
        ("2", _("Bad")),
        ("3", _("Normal")),
        ("4", _("Good")),
        ("5", _("Very Good")),
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
