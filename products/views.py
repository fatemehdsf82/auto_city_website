from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.utils.translation import gettext as _
from products.forms import CommentForm
from .models import Product, Comment
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from cart.forms import AddToCartProductForm


# class ProductListView(generic.ListView):
#     # model = Product
#     queryset = Product.objects.filter(status=True)
#     template_name = "products/product_list.html"
#     context_object_name = "products"


def product_list_view(request):
    product_list = Product.objects.filter(status=True)
    paginator = Paginator(product_list, 6)

    page = request.GET.get("page")
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "products/product_list.html", {"products": products})


class ProductDetatilView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        # context["add_to_cart_form"] = AddToCartProductForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs["product_id"])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        messages.success(self.request, _("comment successfully created"))

        return super().form_valid(form)


def category_view(request, tag):
    products = Product.objects.filter(tags__slug=tag)
    return render(request, "products/product_list.html", {"products": products})
