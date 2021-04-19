"""Morvarid_Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Morvarid_Store import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store_main.urls', namespace='store_main')),
    path('', include('store_account.urls', namespace='store_account')),
    path('', include('store_shop.urls', namespace='store_shop')),
    path('', include('store_contact.urls', namespace='store_contact')),
    path('', include('store_favorite.urls', namespace='store_favorite')),
    path('', include('store_comment.urls', namespace='store_comment')),
    path('', include('store_cart.urls', namespace='store_cart')),
    path('', include('store_ticket.urls', namespace='store_ticket')),
    path('', include('store_setting.urls', namespace='store_setting')),
]

