from django.contrib import admin
from .models import Category, InventoryItem

# Register your models here.

admin.site.register(Category)
admin.site.register(InventoryItem)