from django.contrib import admin
from .models import Blog, Profile


# First Model
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at", "modified_at", "status")


@admin.register(Profile)
class ProfileInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "family_name", "address", "phone_number", "email")
