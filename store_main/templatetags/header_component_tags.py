from django import template
from store_main.forms import LoginForm, RegisterForm
from store_shop.models import Category

register = template.Library()


@register.inclusion_tag('shared/login_component.html')
def login_component():
    login_form = LoginForm()
    register_form = RegisterForm()

    context = {
        'login_form': login_form,
        'register_form': register_form,
    }
    return context


@register.inclusion_tag('shared/nav_header_component.html')
def nav_header_component():
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return context
