from django.contrib import admin
from .models import Blog


# First Model
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at", "modified_at", "status")
