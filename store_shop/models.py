import os
from datetime import datetime
from django.db import models
from django.urls import reverse


def upload_product_image(instance, filename):
    filename = os.path.basename(filename)
    filebase, extension = filename.rsplit('.', maxsplit=1)

    return f'{instance.title}.{extension}'


class ActiveProductManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProductManager, self).get_queryset().filter(is_active=True)


class ActiveExistsProductManager(models.Manager):
    def get_queryset(self):
        return super(ActiveExistsProductManager, self).get_queryset().filter(is_active=True, is_available=True)


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضبحات')
    price = models.PositiveBigIntegerField(verbose_name='قیمت', default=0.0)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال', default=True)
    is_available = models.BooleanField(verbose_name='موجود / نا موجود', default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='categoryproducts')
    feature = models.ManyToManyField('Feature', blank=True, related_name='featureproducts')
    tag = models.ManyToManyField('Tag', blank=True, related_name='tagproducts')
    visit = models.IntegerField(verbose_name='بازدید ها', default=0)
    register_date = models.DateTimeField()
    image = models.ImageField(verbose_name='تصویر اصلی', upload_to=upload_product_image)
    gallery = models.ManyToManyField('Gallery', verbose_name="گالری تصاویر", related_name='galleryproducts')

    objects = models.Manager()
    actived = ActiveProductManager()
    active_and_exists = ActiveExistsProductManager()

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store_shop:product_detail', args=[self.id, self.title.replace(" ", "-")])


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store_shop:product_list_category', args=[self.slug])


class Feature(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


def upload_gallery_image(instance, filename):
    filename = os.path.basename(filename)
    filebase, extension = filename.rsplit('.', maxsplit=1)
    times = datetime.now().strftime('%Y-%m-%d___%H-%M-%S')

    return f'images/product_images/gallery_image/{times}.{extension}'


class Gallery(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام تگ')

    def __str__(self):
        return self.title
