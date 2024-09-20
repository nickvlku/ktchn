from django.db import models
from core.custom_fields import ProductIdField, ProductTypeIdField, SoftDeletionModel

class ProductType(SoftDeletionModel):
    id = ProductTypeIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(SoftDeletionModel):
    id = ProductIdField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.brand} {self.name}" if self.brand else self.name