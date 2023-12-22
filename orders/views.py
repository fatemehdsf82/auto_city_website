from django.shortcuts import render
from flask import redirect
from django.contrib import messages
from cart.cart import Cart
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import OrderItem
from django.utils.translation import gettext as _


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(
            request,
            _("you can not proceed to checkout page because your cart is empty."),
        )
        return redirect("product_list")

    if request.method == "POST":
        order_form = OrderForm(
            request.POST,
        )

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item["product_obj"]
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item["quantity"],
                    price=product.price,
                )

            cart.clear()
            messages.success(request, _("your order has successfully placed."))
            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

    return render(
        request,
        "orders/order_create.html",
        {
            "form": order_form,
        },
    )
