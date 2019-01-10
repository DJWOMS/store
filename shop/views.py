from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductsList(ListView):
    """Список всех продуктов"""
    model = Product
    template_name = "shop/list-product.html"
