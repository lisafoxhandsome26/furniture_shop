from django.urls import path
from orders import views as v

app_name = "orders"

urlpatterns = [
    path('create-order/', v.create_order, name="create_order"),
]
