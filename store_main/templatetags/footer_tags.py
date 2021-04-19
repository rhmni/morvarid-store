from django import template
from store_main.forms import NeewsletterForm
from store_setting.models import Setting

register = template.Library()


@register.inclusion_tag('shared/footer.html')
def footer_component():
    setting = Setting.objects.last()
    form = NeewsletterForm()
    context = {
        'setting': setting,
        'form': form,
    }
    return context
