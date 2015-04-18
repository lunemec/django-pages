# -*- encoding: utf-8 -*-

from django.contrib import admin


class SiteAdmin(admin.ModelAdmin):
    list_display = ('domain', 'display_name', 'tagline')

    class Media:
        js = [
            '/static/admin/js/ckeditor/ckeditor.js',
            '/static/admin/js/ckeditor/start.js',
            '/static/filebrowser/js/FB_CKEditor.js',
        ]

        css = {
            'ckeditor': ('/static/admin/js/ckeditor/contents.css',),
        }


class ScriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
