from django.contrib import admin
from .models import Product, Category, Feature, Gallery, Tag

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(Feature)
admin.site.register(Tag)
