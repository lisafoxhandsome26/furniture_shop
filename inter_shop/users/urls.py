from django.urls import path
from users import views as v

app_name = "users"

urlpatterns = [
    path('login/', v.login, name='login'),
    path('registration/', v.registration, name='registration'),
    path('logout/', v.logout, name='logout'),
    path('profile/', v.profile, name='profile'),
]
