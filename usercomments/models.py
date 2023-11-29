from django.db import models
from datetime import datetime


class Comment(models.Model):
    costumer_Fid = models.ForeignKey("costumers.Costumer",on_delete=models.CASCADE,default=0,name="costumer_id")
    product_Fid = models.ForeignKey("products.Product",on_delete=models.CASCADE,default=0,name="product_id")
    comment_text = models.TextField(max_length=2000,name="comment")
    comment_created_at = models.DateTimeField(datetime.now,name="created_at")
    comment_updated_at = models.DateTimeField(auto_now=True, null=True)

    # def __str__(self):
    #     return self.comment