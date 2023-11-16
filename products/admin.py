from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_cost", "product_category",
                    "product_stock", "product_brand", "product_created_at")

admin.site.register(Product, ProductAdmin)