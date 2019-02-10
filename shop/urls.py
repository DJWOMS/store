from django.urls import path

from . import views


urlpatterns = [
    path("", views.ProductsList.as_view(), name="product_all"),
    path('detail/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path("add-cart-item/<slug:slug>/<int:pk>/", views.AddCartItem.as_view(), name="add_cartitem"),
    path("cart/", views.CartItemList.as_view(), name="cart_item"),
    path("delete/<int:pk>/", views.RemoveCartItem.as_view(), name="del_item"),
    path("edit/<int:pk>/", views.EditCartItem.as_view(), name="edit_item"),
    path("search/", views.Search.as_view(), name="search"),
    path("add-order/", views.AddOrder.as_view(), name="add_order"),
    path("orders/", views.OrderList.as_view(), name="orders"),
    path("checkout/<int:pk>/", views.CheckOut.as_view(), name="checkout"),
    path("category/<slug:slug>/", views.CategoryProduct.as_view(), name="category"),
    path("category-vue/", views.CategoryProductVue.as_view(), name="category_vue"),
    path("sort/", views.SortProducts.as_view(), name="sort"),
]