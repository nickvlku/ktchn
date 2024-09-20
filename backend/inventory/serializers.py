from rest_framework import serializers
from .models import InventoryItem

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'quantity', 'expiration_date', 'user', 'household', 'product', 'created_at', 'updated_at']