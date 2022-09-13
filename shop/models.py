import decimal

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class BrandModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class SizeModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class ColorModel(models.Model):
    code = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'





class ProductModel(models.Model):
    category = models.ForeignKey(
        CategoryModel, on_delete=models.RESTRICT,
        related_name='products',
        verbose_name=_('category')
    )
    title = models.CharField(max_length=60, verbose_name=_('title'))
    short_description = models.CharField(max_length=255, verbose_name=_('short_description'))
    long_description = RichTextUploadingField(verbose_name=_('long_description'))
    price = models.FloatField(verbose_name=_('price'))
    sale = models.PositiveSmallIntegerField(default=0, verbose_name=_('sale'))
    main_image = models.ImageField(upload_to='products/', verbose_name=_('main_image'))
    tag = models.ManyToManyField(ProductTagModel,related_name='products',verbose_name=_('tags'))
    sizes = models.ManyToManyField(SizeModel, related_name='products', verbose_name=_('sizes'))
    brands = models.ForeignKey(BrandModel, on_delete=models.RESTRICT,related_name='products', verbose_name=_('brands'), null=True)
    colors = models.ManyToManyField(ColorModel, related_name='products', verbose_name=_('colors'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_price(self):
        if self.sale:
            return ((100 - self.sale) / 100) * self.sale
        return self.price

    def is_sale(self):
        return bool(self.sale)

    def is_new(self):
        return (timezone.now() - self.created_at).days <= 5

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
