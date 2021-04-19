from django.urls import path
from store_comment.views import add_comment, add_reply_comment

app_name = 'store_comment'
urlpatterns = [
    path('add-comment/<int:product_id>/', add_comment, name='add_comment'),
    path('add-comment/<int:product_id>/<int:comment_id>', add_reply_comment, name='add_reply_comment'),
]
