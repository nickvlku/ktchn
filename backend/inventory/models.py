from django.db import models
from django.conf import settings
import uuid

class InventoryItem(models.Model):
    id = models.CharField(max_length=32, primary_key=True, editable=False)
    quantity = models.IntegerField()
    expiration_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='inventory_items'
    )
    household = models.ForeignKey('households.Household', on_delete=models.CASCADE, related_name='inventory_items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='inventory_items')

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"II{uuid.uuid4().hex[:30]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"