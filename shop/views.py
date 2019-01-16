from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from Store import settings
from .models import Product, Cart, CartItem
from .forms import CartItemForm


class ProductsList(ListView):
    """Список всех продуктов"""
    model = Product
    template_name = "shop/list-product.html"


class ProductDetail(DetailView):
    """Карточка товара"""
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CartItemForm()
        return context


class AddCartItem(View):
    """Добавление товара в карзину"""
    def post(self, request, slug, pk):
        form = CartItemForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.product_id = pk
            form.cart = Cart.objects.get(user=request.user, accepted=False)
            form.save()
            messages.add_message(request, settings.MY_INFO, "Товар добавлен")
            return redirect("/detail/{}/".format(slug))
        else:
            messages.add_message(request, settings.MY_INFO, "Error")
            return redirect("/detail/{}/".format(slug))


class CartItemList(ListView):
    template_name = 'shop/cart.html'

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user, cart__accepted=False)







