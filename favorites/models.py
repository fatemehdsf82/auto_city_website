from django.db import models


class Favorite(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    costumer_Fid = models.ForeignKey("costumers.Costumer",on_delete=models.CASCADE,default=0,name="costumer_id")
    product_Fid = models.ForeignKey("products.Product",on_delete=models.CASCADE,default=0,name="product_id")
    
    