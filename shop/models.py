import decimal

from django.contrib.auth import get_user_model
from django.db import models, IntegrityError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

UserModel = get_user_model()


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
    real_price = models.FloatField(verbose_name=_('real_price'), default=0)
    sale = models.BooleanField(verbose_name=_('sale'), default=False)
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_('discount'))
    main_image = models.ImageField(upload_to='products/', verbose_name=_('main_image'))
    tag = models.ManyToManyField(ProductTagModel,related_name='products',verbose_name=_('tags'))
    sizes = models.ManyToManyField(SizeModel, related_name='products', verbose_name=_('sizes'))
    brands = models.ForeignKey(BrandModel, on_delete=models.RESTRICT,related_name='products', verbose_name=_('brands'), null=True)
    colors = models.ManyToManyField(ColorModel, related_name='products', verbose_name=_('colors'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def new(self):
        return (timezone.now() - self.created_at).days <= 5

    def is_discount(self):
        return bool(self.discount)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class WishlistModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='wishlists', verbose_name=_('user'))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name=_('product'))

    @staticmethod
    def create_or_delete(user, product):
        try:
            return WishlistModel.objects.create(user=user, product=product)
        except IntegrityError:
            return WishlistModel.objects.get(user=user, product=product).delete()

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.product.title}"

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'
        unique_together = 'user', 'product',

