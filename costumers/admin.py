from django.contrib import admin
from .models import Costumer


class CostumerAdmin(admin.ModelAdmin):
    list_display = ("name", "family_name", "Email", 
                    "phone", "address", "postal_code",
                    "created_at")

admin.site.register(Costumer, CostumerAdmin)