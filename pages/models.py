from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
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
