from django import template

register = template.Library()


@register.filter
def price(value):
    return '{:,}'.format(value)
