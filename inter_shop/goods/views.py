from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from .models import Products
from django.http import Http404


def catalog(request, categories_slug):
    page = request.GET.get("page", 1)
    if categories_slug == "All":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=categories_slug))
    paginator = Paginator(goods, 3)
    curent_page = paginator.page(int(page))
    context = {
        "title": "Home - Каталог",
        "goods": curent_page,
        "slug_url": categories_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    prod = Products.objects.get(slug=product_slug)
    context = {
        "product": prod,
    }
    return render(request, "goods/product.html", context)
