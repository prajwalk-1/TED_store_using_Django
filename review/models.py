from django.db import models
from product.models import Product

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    user_profile_pic_url = models.URLField()
    user_joined_date = models.DateField()
    rating = models.IntegerField()
    review_date = models.DateField()
    review_text = models.TextField()
    review_likes = models.IntegerField()

