from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from store_main.forms import NeewsletterForm
from store_setting.models import Setting


class AboutUs(TemplateView):
    template_name = 'store_setting/about_us.html'
    setting = Setting.objects.last()
    extra_context = {
        'title': 'درباره ما',
        'setting': setting,
    }


@require_POST
def newletter(request):
    form = NeewsletterForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.register_date = datetime.now()
        new_form.save()
        messages.success(request, "شما با موفقیت در خبرنامه عضو شدید", 'success')

    return redirect('store_main:home')
