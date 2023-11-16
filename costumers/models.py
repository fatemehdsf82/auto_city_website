from django.db import models
from datetime import datetime



class Costumer(models.Model):
    costumer_id = models.AutoField(primary_key=True)
    costumer_name = models.CharField(max_length=100)
    costumer_family_name = models.CharField(max_length=100)
    costumer_email = models.EmailField(max_length=70,unique=True)
    costumer_phone = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=1000)
    customer_postal_code = models.CharField(max_length=10,unique=True)
    costumer_created_at = models.DateTimeField(datetime.now)
    costumer_updated_at = models.DateTimeField(auto_now=True, null=True)