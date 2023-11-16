from django.contrib import admin
from .models import Costumer


class CostumerAdmin(admin.ModelAdmin):
    list_display = ("costumer_name", "costumer_family_name", "costumer_email", 
                    "costumer_phone", "customer_address", "customer_postal_code",
                    "costumer_created_at")

admin.site.register(Costumer, CostumerAdmin)