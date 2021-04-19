from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from store_ticket.forms import AddTicketForm
from store_ticket.models import Ticket


@login_required
def tickets(request):
    ticket_list = Ticket.objects.filter(Q(from_user=request.user) | Q(to_user=request.user)).distinct()
    form = AddTicketForm()

    context = {
        'title': 'پشتیبانی',
        'ticket_list': ticket_list,
        'form': form,
    }
    return render(request, 'store_ticket/ticket.html', context)


@login_required
@require_POST
def add_ticket(request):
    form = AddTicketForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        Ticket.objects.create(from_user=request.user, text=text, send_date=datetime.now())
        messages.success(request, 'پیام شما با موفقیت ارسال شد', 'success')

    return redirect('store_ticket:tickets')
