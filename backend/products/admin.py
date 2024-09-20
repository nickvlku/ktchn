from django.contrib import admin
from .models import Product, ProductType

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'deleted')
    list_filter = ('deleted',)
    search_fields = ('name',)
    readonly_fields = ('id', 'created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'product_type', 'created_at', 'updated_at', 'deleted')
    list_filter = ('deleted', 'product_type')
    search_fields = ('name', 'brand')
    readonly_fields = ('id', 'created_at', 'updated_at')