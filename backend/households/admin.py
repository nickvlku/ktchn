from django.contrib import admin
from .models import Household

@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'deleted')
    list_filter = ('deleted',)
    search_fields = ('name',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    filter_horizontal = ('users',)