from django import forms

from .models import CartItem


class CartItemForm(forms.ModelForm):
    """Форма добавления товара"""
    class Meta:
        model = CartItem
        fields = ("quantity",)