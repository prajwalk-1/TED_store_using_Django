from django.db import models

# Create your models here.
from product.models import Product

class Order(models.Model):
    user_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

