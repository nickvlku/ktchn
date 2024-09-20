from django.db import models
import uuid

class CustomIdField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 32
        kwargs['unique'] = True
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if add and not self.value_from_object(model_instance):
            prefix = self.get_prefix(model_instance)
            value = f"{prefix}{uuid.uuid4().hex[:30]}"
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)

    def get_prefix(self, model_instance):
        raise NotImplementedError("Subclasses must implement get_prefix()")

class UserIdField(CustomIdField):
    def get_prefix(self, model_instance):
        return "US"

class HouseholdIdField(CustomIdField):
    def get_prefix(self, model_instance):
        return "HO"

class InventoryItemIdField(CustomIdField):
    def get_prefix(self, model_instance):
        return "II"

class ProductIdField(CustomIdField):
    def get_prefix(self, model_instance):
        return "PR"

class ProductTypeIdField(CustomIdField):
    def get_prefix(self, model_instance):
        return "PT"

class SoftDeletionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class SoftDeletionModel(models.Model):
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeletionManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super().delete()