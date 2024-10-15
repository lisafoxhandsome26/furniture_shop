from django.urls import path
from goods import views as v

app_name = "goods"

urlpatterns = [
    path('search/', v.CatalogView.as_view(), name='search'),
    path('<slug:categories_slug>/', v.CatalogView.as_view(), name='index'),
    path('product/<slug:product_slug>/', v.ProductView.as_view(), name='product'),
]
