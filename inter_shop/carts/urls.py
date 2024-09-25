from django.urls import path
from carts import views as v

app_name = "carts"

urlpatterns = [
    path('cart_add/', v.cart_add, name='cart_add'),
    path('cart_change/', v.cart_change, name='cart_change'),
    path('cart_remove/', v.cart_remove, name='cart_remove'),
]
