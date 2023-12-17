from django.urls import path

from .views import cart_detail_view, add_to_cart_view, remove_from_cart_view

urlpatterns = [
    path("", cart_detail_view, name="cart_detail"),
    path("add/<int:product_id>/", add_to_cart_view, name="cart_add"),
    path("remove/<int:product_id>/", remove_from_cart_view, name="cart_remove"),
]
