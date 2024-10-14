from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'product_id', 'quantity')
    list_display_links = ('id', 'user_id')
    list_filter = ('quantity','user_id')
    search_fields = ('user_id', 'product_id__product_title', 'quantity')
    ordering = ('user_id',)

admin.site.register(Order, OrderAdmin)
