from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (Category, Product, Cart, CartItem, Order)


class CategoryMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class CartItemAdmin(admin.ModelAdmin):
    """Товары в корзине"""
    list_display = ("cart", "product", "quantity")


admin.site.register(Category, CategoryMPTTModelAdmin)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order)
