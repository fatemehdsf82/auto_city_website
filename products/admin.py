from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "cost", "category",
                    "stock", "brand", "created_at")

admin.site.register(Product, ProductAdmin)