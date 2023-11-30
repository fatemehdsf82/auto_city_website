from django.db import models
from datetime import datetime


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
    product_description = models.TextField(null=True)
    product_cost = models.PositiveIntegerField(name="cost")
    product_category = models.CharField(
        max_length=40, choices=CATEGORY_CHOICES, name="category"
    )
    product_brand = models.CharField(
        max_length=40, choices=BRAND_CHOICES, default="blank", name="brand"
    )
    product_stock = models.IntegerField(default=0, name="stock")
    #! status added
    product_status = models.BooleanField(default=True)

    # previous datetime
    product_created_at = models.DateTimeField(datetime.now, name="created_at")
    product_updated_at = models.DateTimeField(auto_now=True, null=True)
    # image = models.ImageField(upload_to='product_images/bolboring.jpg',width_field=600,height_field=600, default='product_images/bolboring.jpg')

    # ? new datetime
    # datetime_created = models.DateTimeField(auto_now_add=True)
    # datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
