# -*- encoding: utf-8 -*-

from django.conf.urls import patterns
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from django_pages.views import main_view
from ..common.admin_actions import activate, deactivate, enable_comments, disable_comments
from .models import Page, Post


class PreviewAdmin(admin.ModelAdmin):
    """
    Custom parent class, with preview support
    """
    readonly_fields = ['preview_link', ]

    class Media:
        js = [
            '/static/admin/js/ckeditor/ckeditor.js',
            '/static/admin/js/ckeditor/start.js',
            '/static/filebrowser/js/FB_CKEditor.js',
        ]
        css = {
            'ckeditor': ('/static/admin/js/ckeditor/contents.css',),
        }

    def get_urls(self):
        admin_view = self.admin_site.admin_view
        urls = patterns('',
                        (r'^(?P<item_pk>\d+)/preview/$', admin_view(self.preview_view)),
                        )

        return urls + super(PreviewAdmin, self).get_urls()

    def preview_link(self, obj):
        """
        Returns url for page preview

        @return string
        """
        return '<a href="./preview/">Page preview</a>'

    preview_link.allow_tags = True
    preview_link.short_description = 'Preview'

    def preview_view(self, request, item_pk):
        pass


class PageAdmin(PreviewAdmin):

    fieldsets = (
        (None, {
            'fields': (('title', 'link'), 'content', 'active', 'index', 'preview_link')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('metadata_set',)
        }),
    )

    list_editable = ('link', 'active', 'metadata_set')
    list_display = ('title', 'link', 'active', 'metadata_set', 'items_per_menu')
    list_filter = ('active', 'index')
    search_fields = ('title', 'content', 'link__menuitem_name')
    actions = [activate, deactivate]

    def preview_view(self, request, item_pk):
        if self.has_change_permission(request):
            item = get_object_or_404(Page, pk=item_pk)
            item.active = False
            item.save()

            url = item.get_url()[1:]

            return main_view(request, url, preview=True)

        raise PermissionDenied


class PostAdmin(PreviewAdmin):

    fields = (('title', 'page'), 'content', 'active', 'comments', 'preview_link', 'visible_from', 'visible_to', 'created')
    list_editable = ('page', 'active', 'visible_from', 'visible_to', 'comments')
    list_display = ('title', 'page', 'active', 'visible_from', 'visible_to', 'comments')
    list_filter = ('active', 'page')
    search_fields = ['title', 'content', 'page__title']
    actions = [activate, deactivate, enable_comments, disable_comments]

    def preview_view(self, request, item_pk):
        if self.has_change_permission(request):
            item = get_object_or_404(Post, pk=item_pk)
            item.active = False
            item.save()

            url = item.get_url()[1:]

            return main_view(request, url, preview=True)

        raise PermissionDenied
