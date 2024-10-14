from django.contrib import admin
from .models import ProductReview

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'product_id', 'rating', 'review_date')
    list_display_links = ('id', 'user_id')
    list_filter = ('rating', 'review_date')
    search_fields = ('user_id', 'product_id__product_title', 'rating')
    ordering = ('review_date',)

admin.site.register(ProductReview, ProductReviewAdmin)
