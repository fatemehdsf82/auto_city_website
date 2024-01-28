from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from products.models import Product
from .favorite import Favorite
from .forms import AddToFavoriteProductForm
from django.contrib import messages
from django.utils.translation import gettext as _


def favorite_detail_view(request):
    favorite = Favorite(request)
    for item in favorite:
        item["product_update_quantity_form"] = AddToFavoriteProductForm(
            initial={
                "quantity": item["quantity"],
                "inplace": True,
            }
        )
    return render(
        request,
        "favorites/favorite.html",
        {
            "favorite": favorite,
        },
    )


@require_POST
def add_to_favorite_view(request, product_id):
    favorite = Favorite(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToFavoriteProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data["quantity"]
        favorite.add(
            product, quantity, replace_current_quantity=cleaned_data["inplace"]
        )

    return redirect("product_list")


def remove_from_favorite_view(request, product_id):
    favorite = Favorite(request)
    product = get_object_or_404(Product, id=product_id)
    favorite.remove(product)
    return redirect("favorite_detail")


@require_POST
def clear_favorite(request):
    favorite = Favorite(request)
    if len(favorite):
        favorite.clear()
        messages.success(
            request, _("all products successfully removed from your wishlist.")
        )
    else:
        messages.warning(request, _("your favorite is already empty."))

    return redirect("product_list")
