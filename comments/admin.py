from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("costumer_id", "product_id", "comment", "created_at")

admin.site.register(Comment, CommentAdmin)