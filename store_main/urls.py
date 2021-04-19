
from django.urls import path
from .views import Home, login_user, logout_user, register_user

app_name = 'store_main'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login-user', login_user, name='login_user'),
    path('register-user', register_user, name='register_user'),
    path('logout', logout_user, name='logout'),
]


