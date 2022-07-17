from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class AutherModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_('full_name'))
    image = models.ImageField(upload_to='auther_images', verbose_name=_('image'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')



class PostTagModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')



class PostModel(models.Model):
    author = models.ForeignKey(AutherModel, on_delete=models.RESTRICT)
    title = models.CharField(max_length=255, verbose_name=_('title'))
    body = RichTextUploadingField(verbose_name=_('body'))
    main_image = models.ImageField(upload_to='main_images', verbose_name=_('main_image'))
    banner = models.ImageField(upload_to='post_banners', verbose_name=_('banner'))
    tag = models.ManyToManyField(PostTagModel, related_name='posts', verbose_name=_('tag'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f"{self.title[:100]} ..."

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')



class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments', verbose_name=_('comment'))
    name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')