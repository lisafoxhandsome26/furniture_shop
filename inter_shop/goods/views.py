from django.views.generic import DetailView, ListView

from .models import Products, Categories
from .utils import q_search


class ProductView(DetailView):
    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context


class CatalogView(ListView):
    model = Products
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 3
    allow_empty = False

    def get_queryset(self):
        categories_slug = self.kwargs.get("categories_slug")
        on_sale = self.request.GET.get("on_sale", None)
        order_by = self.request.GET.get("order_by", None)
        query = self.request.GET.get("q", None)

        if categories_slug == "All":
            goods = super().get_queryset()
        elif query:
            goods = q_search(query)
        else:
            goods = super().get_queryset().filter(category__slug=categories_slug)
        if on_sale:
            goods = goods.filter(discount__gt=0)
        if order_by and order_by != 'default':
            goods = goods.order_by(order_by)

        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Каталог"
        context["slug_url"] = self.kwargs.get("categories_slug")
        return context


def catalog(request, categories_slug=None):
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)
    if categories_slug == "All":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=categories_slug))
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)
    paginator = Paginator(goods, 3)
    curent_page = paginator.page(int(page))
    context = {
        "title": "Home - Каталог",
        "goods": curent_page,
        "slug_url": categories_slug,
    }
    return render(request, "goods/catalog.html", context)


# def product(request, product_slug):
#     prod = Products.objects.get(slug=product_slug)
#     context = {
#         "product": prod,
#     }
#     return render(request, "goods/product.html", context)
