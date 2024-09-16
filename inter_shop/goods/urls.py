from django.urls import path
from goods import views as v

app_name = "goods"

urlpatterns = [
    path('search/', v.catalog, name='search'),
    path('<slug:categories_slug>/', v.catalog, name='index'),
    path('product/<slug:product_slug>/', v.product, name='product'),
]
