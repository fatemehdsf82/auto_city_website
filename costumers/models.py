from django.db import models
from datetime import datetime



class Costumer(models.Model):
    costumer_id = models.AutoField(primary_key=True)
    costumer_name = models.CharField(max_length=100,name="name")
    costumer_family_name = models.CharField(max_length=100,name="family_name")
    costumer_email = models.EmailField(max_length=70,unique=True,name="Email")
    costumer_phone = models.CharField(max_length=20,name="phone")
    customer_address = models.CharField(max_length=1000,name="address")
    customer_postal_code = models.CharField(max_length=10,unique=True,name="postal_code")
    costumer_created_at = models.DateTimeField(datetime.now,name="created_at")
    costumer_updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name +" "+ self.family_name
