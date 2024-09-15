from django.urls import path
from goods import views as v

app_name = "goods"

urlpatterns = [
    path('<slug:categories_slug>/', v.catalog, name='index'),
    path('<slug:categories_slug>/<int:page>/', v.catalog, name='index'),
    path('product/<slug:product_slug>/', v.product, name='product'),
]
