from django.shortcuts import render, get_object_or_404
from .models import Products


def catalog(request, categories_slug):
    if categories_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=categories_slug))
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    prod = Products.objects.get(slug=product_slug)
    context = {
        "product": prod,
    }
    return render(request, "goods/product.html", context)
