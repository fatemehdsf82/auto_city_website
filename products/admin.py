from django.contrib import admin
from .models import Product, Comment, Tag


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "stock",
        "brand",
        "status",
        "modified_at",
    )


@admin.register(Tag)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product", "author", "text", "star", "active")
