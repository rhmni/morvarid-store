from django.urls import path

from .views import AboutUs, newletter

app_name = 'store_setting'

urlpatterns = [
    path('about-us', AboutUs.as_view(), name='about_us'),
    path('newsletter', newletter, name='newsletter'),
]
