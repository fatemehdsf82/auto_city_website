from django.views import generic
from .models import Product


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(status=True)
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductDetatilView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"
