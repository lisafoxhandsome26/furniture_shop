from django.urls import path
from users import views as v

app_name = "users"

urlpatterns = [
    path('login/', v.UserLoginView.as_view(), name='login'),
    path('registration/', v.UserRegistrationView.as_view(), name='registration'),
    path('logout/', v.logout, name='logout'),
    path('profile/', v.UserProfileView.as_view(), name='profile'),
    path('users-cart/', v.UserCartView.as_view(), name='users_cart'),
]
