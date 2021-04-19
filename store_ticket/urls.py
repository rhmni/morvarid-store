from django.urls import path

from store_ticket.views import tickets,add_ticket

app_name = 'store_ticket'
urlpatterns = [
    path('tickets', tickets, name='tickets'),
    path('add-ticket', add_ticket, name='add_ticket'),
]
