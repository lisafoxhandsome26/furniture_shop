from django.urls import path
from main import views as v

app_name = "main"

urlpatterns = [
    path('about/', v.about, name='about'),
    path('', v.index, name='index'),
]
