from django.db import models
from django.conf import settings
import uuid

class Household(models.Model):
    id = models.CharField(max_length=32, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='households'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f"HO{uuid.uuid4().hex[:30]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name