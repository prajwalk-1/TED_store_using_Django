from django.contrib import admin
from .models import Product, ProductDetails, Tag

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_title', 'product_price')
    list_display_links = ('id', 'product_title')
    list_filter = ('product_price','id')
    search_fields = ('product_title', 'product_price')
    ordering = ('product_price',)

class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_base_price', 'product_discounted_price', 'in_stock')
    list_display_links = ('product',)
    list_filter = ('product_base_price', 'product_discounted_price')
    search_fields = ('product__product_title', 'product_base_price', 'product_discounted_price')
    ordering = ('product_base_price',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetails, ProductDetailsAdmin)
admin.site.register(Tag)
