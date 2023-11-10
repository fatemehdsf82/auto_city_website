from django.db import models

# just for test    
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()