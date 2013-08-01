# -*- encoding: utf-8 -*-

from django.contrib import admin

import reversion

from ..common.admin_actions import activate, deactivate


class PageAdmin(reversion.VersionAdmin):

    fieldsets = (
        (None, {
            'fields': (('title', 'link'), 'content', 'active', 'index')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('metadata_set',)
        }),
    )

    list_display = ('title', 'link', 'active', 'metadata_set')
    actions = [activate, deactivate]

    class Media:

        js = [
            '/static/admin/js/ckeditor/ckeditor.js',
            '/static/admin/js/ckeditor/config.js',
            '/static/admin/js/ckeditor/start.js',
        ]

        css = {
            'ckeditor': ('/static/admin/js/ckeditor/contents.css',),
        }


class PostAdmin(reversion.VersionAdmin):

    fields = (('title', 'page'), 'content', 'active', 'comments', 'visible_from', 'visible_to', 'created')
    list_display = ('title', 'page', 'active')
    actions = [activate, deactivate]

    class Media:

        js = [
            '/static/admin/js/ckeditor/ckeditor.js',
            '/static/admin/js/ckeditor/config.js',
            '/static/admin/js/ckeditor/start.js',
        ]

        css = {
            'ckeditor': ('/static/admin/js/ckeditor/contents.css',),
        }
