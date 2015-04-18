# -*- encoding: utf-8 -*-

from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'user', 'post', 'ip')
    list_display_links = ('id', 'comment')
    list_filter = ('user', 'post', 'ip')
    search_fields = ['user', 'post__title', 'ip']
