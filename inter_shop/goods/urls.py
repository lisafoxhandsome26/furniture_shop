from django.urls import path
from goods import views as v

app_name = "goods"

urlpatterns = [
    path('', v.catalog, name='index'),
    path('product/', v.product, name='product'),
]
