from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import TemplateView
from store_main.forms import LoginForm, RegisterForm
from store_setting.models import Setting
from store_shop.forms import SearchForm
from store_shop.models import Product, Category
from store_user.models import User
import random


def login_user(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        data = login_form.cleaned_data
        user = authenticate(email=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            messages.success(request, 'شما با موفقیت وارد حساب کاربری شدید.', 'success')
        else:
            messages.error(request, 'کاربری با این مشخصات یافت نشد.', 'error')
    return redirect('store_main:home')


class Home(TemplateView):
    template_name = 'store_main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        search_form = SearchForm()
        setting = Setting.objects.last()
        most_visited_product = Product.actived.order_by('-visit')[:6]
        most_inexpensive_product = Product.actived.order_by('price')[:6]
        most_popular_category = Category.objects.all().order_by()
        most_popular_category = random.choices(most_popular_category, k=10)
        context.update({
            'title': 'فروشگاه مروارید',
            'search_form': search_form,
            'setting': setting,
            'most_visited_product': most_visited_product,
            'most_inexpensive_product': most_inexpensive_product,
            'most_popular_category': most_popular_category,
        })
        return context


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'شما با موفقیت از حساب کاربری خارج شدید', 'success')
    return redirect('store_main:home')


def register_user(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        data = register_form.cleaned_data

        user = User.objects.create_user(email=data['email'], first_name=data['first_name'], last_name=data['last_name'],
                                        password=data['password1'])
        user.join_date = datetime.now()
        user.save()
        messages.success(request, 'شما با موفقیت ثبت نام کردید اکنون میتوانید وارد شوید', 'success')
        return redirect('store_main:home')

    return redirect('store_main:home')
