from django.urls import path

from store_contact.views import ContactUsPage

app_name = 'store_contact'
urlpatterns = [
    path('contact-us', ContactUsPage.as_view(), name='contact_us')
]
