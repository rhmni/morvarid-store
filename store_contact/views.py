from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from store_setting.models import Setting
from .forms import ContactUsForm
from .models import ContactUs


class ContactUsPage(CreateView):
    template_name = 'store_contact/contact_us.html'
    model = ContactUs
    form_class = ContactUsForm
    setting = Setting.objects.last()
    extra_context = {
        'title': 'ارتباط با ما',
        'setting': setting,
    }
    success_url = reverse_lazy('store_main:home')

    def form_valid(self, form):
        messages.success(self.request, 'پیام شما با موفقیت ارسال شد', 'success')
        return super(ContactUsPage, self).form_valid(form)
