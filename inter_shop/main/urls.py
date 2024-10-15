from django.urls import path
from main import views as v

app_name = "main"

urlpatterns = [
    path('about/', v.AboutView.as_view(), name='about'),
    path('', v.IndexView.as_view(), name='index'),
]
