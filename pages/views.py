from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Blog
from products.forms import CommentForm
from .forms import ProductSearchForm
from products.models import Product
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.utils.translation import gettext as _
from django.contrib.auth import login


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


# @login_required
# def profile_view(request):
#     if request.method == "POST":
#         profile_form = ProfileUpdateForm(request.POST, instance=request.user)

#         if profile_form.is_valid():
#             user = profile_form.save(commit=False)
#             user.user = request.user
#             user.save()
#             return redirect("profile")
#     else:
#         profile_form = ProfileUpdateForm()

#     return render(
#         request,
#         "pages/profile.html",
#         {
#             "form": profile_form,
#         },
#     )


@login_required
def profile_view(request):
    profile_form = ProfileUpdateForm()

    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST)

        if profile_form.is_valid():
            user = profile_form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect("profile")
    else:
        profile_form = ProfileUpdateForm()

    return render(
        request,
        "pages/profile.html",
        {
            "form": profile_form,
        },
    )


# @login_required
# def profile_view(request):
#     initial_email = request.user.email if request.user.is_authenticated else ""

#     if request.method == "POST":
#         profile_form = ProfileForm(request.POST)
#         if profile_form.is_valid():
#             user = profile_form.save(commit=False)
#             user.user = request.user
#             user.save()
#             messages.success(request, _("your profile has successfully placed."))
#             return redirect("profile")
#     else:
#         profile_form = ProfileForm(initial={"email": initial_email})

#     return render(
#         request,
#         "pages/profile.html",
#         {
#             "form": profile_form,
#         },
#     )
