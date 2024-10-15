from django.urls import path
from carts import views as v

app_name = "carts"

urlpatterns = [
    path('cart_add/', v.CartAddView.as_view(), name='cart_add'),
    path('cart_change/', v.CartChangeView.as_view(), name='cart_change'),
    path('cart_remove/', v.CartRemoveView.as_view(), name='cart_remove'),
]
