from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Blog


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutUsPageView(TemplateView):
    template_name = "pages/aboutus.html"


class BlogListView(generic.ListView):
    queryset = Blog.objects.filter(status=True)
    template_name = "pages/blog_list.html"
    context_object_name = "blogs"


class BlogDetailView(TemplateView):
    model = Blog
    template_name = "pages/blog_detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["comment_form"] = CommentForm()
        # context["add_to_cart_form"] = AddToCartProductForm()
        return context
