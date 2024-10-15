from django.urls import path
from orders import views as v

app_name = "orders"

urlpatterns = [
    path('create-order/', v.CreateOrderView.as_view(), name="create_order"),
]
