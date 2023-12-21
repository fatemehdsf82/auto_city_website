from django.contrib import admin
from .models import Product, Comment


# First Model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "category",
        "stock",
        "brand",
        "status",
        "modified_at",
    )


# Second Model
# admin.site.register(Product, ProductAdmin)


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product", "author", "text", "star", "active")
