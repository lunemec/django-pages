# -*- encoding: utf-8 -*-

from django.contrib import admin


class SiteAdmin(admin.ModelAdmin):

    list_display = ('domain', 'display_name', 'tagline')

    class Media:

        js = [
            '/static/js/jquery-1.10.2.min.js',
            '/static/admin/js/ckeditor/ckeditor.js',
            '/static/admin/js/ckeditor/adapters/jquery.js',
            '/static/admin/js/ckeditor/config.js',
            '/static/admin/js/ckeditor/start.js',
        ]

        css = {
            'ckeditor': ('/static/admin/js/ckeditor/contents.css',),
        }


class ScriptAdmin(admin.ModelAdmin):

    list_display = ('name', 'code')
