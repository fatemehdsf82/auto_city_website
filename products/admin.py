from django.contrib import admin
from .models import Product


# First Model
# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "cost",
        "category",
        "stock",
        "brand",
        "status",
        "created_at",
        "modified_at",
    )


# Second Model
admin.site.register(Product, ProductAdmin)
