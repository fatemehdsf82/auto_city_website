from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext as _


class Favorite:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        favorite = self.session.get("favorite")

        if not favorite:
            self.session["favorite"] = {}
            favorite = self.session["favorite"]

        self.favorite = favorite

    def add(self, product, quantity=1, replace_current_quantity=False):
        product_id = str(product.id)

        if product_id not in self.favorite:
            self.favorite[product_id] = {"quantity": 0}

        if replace_current_quantity:
            self.favorite[product_id]["quantity"] = quantity
        else:
            self.favorite[product_id]["quantity"] += quantity

        messages.success(self.request, _("product successfully added to wishlist"))
        self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.favorite:
            del self.favorite[product_id]
            messages.success(
                self.request, _("product successfully removed from wishlist")
            )
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.favorite.keys()

        products = Product.objects.filter(id__in=product_ids)

        favorite = self.favorite.copy()

        for product in products:
            favorite[str(product.id)]["product_obj"] = product

        for item in favorite.values():
            item["total_price"] = item["product_obj"].price * item["quantity"]
            yield item

    def __len__(self):
        return len(self.favorite.keys())
        # return sum(item["quantity"] for item in self.favorite.values())

    def clear(self):
        del self.session["favorite"]
        self.save()

    def get_total_price(self):
        product_ids = self.favorite.keys()

        return sum(
            item["quantity"] * item["product_obj"].price
            for item in self.favorite.values()
        )

    def get_total_product(self):
        product_ids = self.favorite.keys()

        return sum(item["quantity"] for item in self.favorite.values())

    def is_empty(self):
        if self.favorite:
            return False
        return True
