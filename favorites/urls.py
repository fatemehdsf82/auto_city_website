from django.urls import path

from .views import (
    favorite_detail_view,
    add_to_favorite_view,
    remove_from_favorite_view,
    clear_favorite,
)

urlpatterns = [
    path("", favorite_detail_view, name="favorite_detail"),
    path("add/<int:product_id>/", add_to_favorite_view, name="favorite_add"),
    path("remove/<int:product_id>/", remove_from_favorite_view, name="favorite_remove"),
    path("clear/", clear_favorite, name="favorite_clear"),
]
