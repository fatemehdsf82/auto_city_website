from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Blog
from products.forms import CommentForm
from .forms import ProductSearchForm
from products.models import Product


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutUsPageView(TemplateView):
    template_name = "pages/aboutus.html"


class BlogListView(generic.ListView):
    queryset = Blog.objects.filter(status=True)
    template_name = "pages/blog_list.html"
    context_object_name = "blogs"


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "pages/blog_detail.html"
    context_object_name = "blog"


def search_view(request):
    form = ProductSearchForm()
    return render(request, "pages/search.html", {"form": form})


def result_view(request):
    form = ProductSearchForm(
        request.GET or None
    )  # Use GET request to maintain pagination links

    if request.method == "GET" and form.is_valid():
        products = Product.objects.all()

        # # Retrieve and convert form data
        # name = form.cleaned_data.get("name")
        # brand = form.cleaned_data.get("brand")
        # tags = form.cleaned_data.get("tags")

    context = {"form": form, "products": products}
    return render(request, "pages/result.html", context)
