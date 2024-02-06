from django.db import models

class Tag(models.Model):
    tags_name = models.CharField(max_length=255)

class Product(models.Model):
    product_title = models.CharField(max_length=255)
    product_description = models.TextField()
    product_image = models.URLField()
    product_rating = models.CharField(max_length=20)
    product_price = models.FloatField()

class ProductDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    product_base_price = models.IntegerField()
    product_discounted_price = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    product_quantity = models.IntegerField()
    product_details = models.TextField()
    product_images = models.URLField()