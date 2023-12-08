from django.urls import path, include
from .views import ProductListView, ProductDetatilView


urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetatilView.as_view(), name="product_detail"),
]
