from django.contrib import admin
from .models import Inventory, Supplier

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'stock', 'availability')

admin.site.register(Supplier)