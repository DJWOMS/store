from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProductsList.as_view(), name="product_all"),
    path('detail/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path("add-cartitem/<slug:slug>/<int:pk>/", views.AddCartItem.as_view(), name="add_cartitem"),
    path("cart/", views.CartItemList.as_view(), name="cart_item"),
]