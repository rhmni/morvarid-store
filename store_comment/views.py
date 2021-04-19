from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from store_comment.forms import AddCommentForm, AddReplyCommentForm
from store_comment.models import Comment
from store_shop.models import Product


@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.writer = request.user
            new_form.product = product
            new_form.created_date = datetime.now()
            new_form.save()

            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')

    return redirect('store_shop:product_detail', product.id, product.title.replace(' ', '-'))


@login_required
def add_reply_comment(request, product_id, comment_id):
    product = get_object_or_404(Product, id=product_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = AddReplyCommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.writer = request.user
            new_form.product = product
            new_form.created_date = datetime.now()
            new_form.reply = comment
            new_form.is_reply = True
            new_form.save()

            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')

    return redirect('store_shop:product_detail', product.id, product.title.replace(' ', '-'))
