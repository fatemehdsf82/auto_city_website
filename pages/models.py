from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings


class Blog(models.Model):
    title = models.CharField(max_length=200, name="title")
    content = models.TextField(name="content")
    post_created_at = models.DateTimeField(datetime.now, name="created_at", blank=True)
    post_updated_at = models.DateTimeField(
        auto_now=True, null=True, name="modified_at", blank=True
    )
    post_status = models.BooleanField(default=True, name="status", blank=True)
    product_image = models.ImageField(
        verbose_name=_("Post Image"),
        upload_to="pages/post_cover/",
        blank=True,
        name="image",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", args=[self.pk])


# class Profile(models.Model):
#     name = models.CharField(max_length=50, blank=True)
#     family_name = models.CharField(max_length=100, blank=True)
#     address = models.TextField(blank=True)
#     phone_number = models.CharField(max_length=11, blank=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.email


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    family_name = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    email = models.EmailField(default=settings.DEFAULT_FROM_EMAIL)
