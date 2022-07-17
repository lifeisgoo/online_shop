from django.contrib import admin
from .models import *


@admin.register(PostTagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title']
    list_filter = ['created_at']
    autocomplete_fields = ['author', 'tag']


@admin.register(CommentModel)
class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    list_display_links = ['name', 'email', 'phone']
    list_filter = ['created_at']


@admin.register(AutherModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']
    search_fields = ['full_name']
