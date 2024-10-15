from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home - Главная"
        context['content'] = "Магазин мебели HOME"

        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home - О нас"
        context['content'] = "О нас"
        context['text_on_page'] = "Текст о том почему этот магазин такой классный"
        return context


# def index(request):
#     context = {
#         "title": "Home - Главная",
#         "content": "Магазин мебели HOME",
#     }
#     return render(request, "main/index.html", context)


# def about(request):
#     context = {
#         "title": "Home - О нас",
#         "content": "О нас",
#         "text_on_page": "Текст о том почему этот магазин такой классный"
#     }
#     return render(request, "main/about.html", context)
