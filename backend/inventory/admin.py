from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'user', 'household', 'expiration_date', 'created_at', 'updated_at', 'deleted')
    list_filter = ('deleted', 'household', 'product__product_type')
    search_fields = ('product__name', 'user__email', 'household__name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    raw_id_fields = ('user', 'household', 'product')