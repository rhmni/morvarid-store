from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from store_cart.forms import AddCartItemForm
from store_comment.forms import AddCommentForm, AddReplyCommentForm
from store_comment.models import Comment
from store_favorite.models import FavoriteRelation
from store_setting.models import Setting
from .forms import SearchForm
from .models import Product, Category


def product_list(request, category=None):
    search_form = SearchForm(initial={'search': request.GET.get('search')})
    categories = Category.objects.all()
    products = Product.actived.all()
    if 'search' in request.GET:
        q = request.GET['search']
        products = products.filter(
            Q(title__icontains=q) | Q(description__icontains=q) | Q(feature__title__icontains=q) | Q(
                tag__title__icontains=q))
    if category:
        products = products.filter(category__slug=category)

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'محصولات',
        'page_obj': page_obj,
        'categories': categories,
        'search_form': search_form,
    }
    return render(request, 'store_shop/product_list.html', context)


class ProductDetail(DetailView):
    template_name = 'store_shop/product_detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        setting = Setting.objects.last()
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        related_products = Product.actived.filter(category=product.category)
        related_products = related_products.exclude(id=product.id)[:6]
        categories = Category.objects.all()
        product.visit += 1
        product.save()
        is_favorite = False

        if self.request.user.is_authenticated:
            favorite_relation = FavoriteRelation.objects.filter(user=self.request.user,
                                                                product__id=self.kwargs['product_id'])
            if favorite_relation.exists():
                is_favorite = True
        comments = Comment.objects.filter(is_reply=False, product=product)
        comment_count = Comment.objects.filter(product=product).count()
        add_comment_form = AddCommentForm()
        add_reply_comment_form = AddReplyCommentForm()
        add_cart_item_form = AddCartItemForm()
        context.update({
            'title': product.title,
            'categories': categories,
            'related_products': related_products,
            'is_favorite': is_favorite,
            'comments': comments,
            'comment_count': comment_count,
            'add_comment_form': add_comment_form,
            'add_reply_comment_form': add_reply_comment_form,
            'add_cart_item_form': add_cart_item_form,
            'setting': setting,

        })
        return context

    def get_queryset(self, **kwargs):
        return Product.actived.filter(id=self.kwargs['product_id'])
