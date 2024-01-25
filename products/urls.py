from django.urls import path, include
from .views import (
    ProductDetatilView,
    CommentCreateView,
    category_view,
    product_list_view,
)


urlpatterns = [
    # path("", ProductListView.as_view(), name="product_list"),
    path("", product_list_view, name="product_list"),
    path("category/<tag>/", category_view, name="category_view"),
    path("<int:pk>/", ProductDetatilView.as_view(), name="product_detail"),
    path(
        "comment/<int:product_id>/", CommentCreateView.as_view(), name="comment_create"
    ),
]
