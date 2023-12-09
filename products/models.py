from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
from django.shortcuts import reverse


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("ghataat_badaneh", "ghataat_badaneh"),
        ("motor_exoz", "motor_exoz"),
        ("barghi_electricy", "barghi_electricy"),
        ("roghan_filter", "roghan_filter"),
        ("ghataat_dakheli", "ghataat_dakheli"),
        ("enteghal_ghodrat", "enteghal_ghodrat"),
        ("farman_jelobandi_tormoz", "farman_jelobandi_tormoz"),
        ("bolboring", "bolboring"),
        ("kasenamad", "kasenamad"),
        ("oring", "oring"),
        ("gardgir", "gardgir"),
        ("looleh", "looleh"),
        ("tasmeh", "tasmeh"),
        ("shelang", "shelang"),
    ]

    BRAND_CHOICES = [
        ("saipa", "saipa"),
        ("mashad_washer", "mashad_washer"),
        ("HIC", "HIC"),
        ("ezaam", "ezaam"),
        ("crouse", "crouse"),
        ("amirnia", "amirnia"),
        ("jaham_lent", "jaham_lent"),
        ("behran", "behran"),
        ("isaco", "isaco"),
    ]
    product_id = models.AutoField(primary_key=True)
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

    product_created_at = models.DateTimeField(datetime.now, name="created_at")
    product_updated_at = models.DateTimeField(
        auto_now=True, null=True, name="modified_at"
    )

    # new datetime
    # datetime_created = models.DateTimeField(auto_now_add=True)
    # datetime_modified = models.DateTimeField(auto_now=True)

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
    body = models.TextField(name="text")
    comment_created_at = models.DateTimeField(datetime.now, name="created_at")
    comment_updated_at = models.DateTimeField(
        auto_now=True, null=True, name="modified_at"
    )

    star = models.CharField(
        max_length=10, choices=PRODUCT_STARS, name="star", default=5
    )
    active = models.BooleanField(default=True)
