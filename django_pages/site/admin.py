# -*- encoding: utf-8 -*-

import reversion


class SiteAdmin(reversion.VersionAdmin):

    list_display = ('domain', 'display_name', 'tagline')

    class Media:

        js = [
            '/static/admin/js/ckeditor/ckeditor.js',
            '/static/admin/js/ckeditor/config.js',
            '/static/admin/js/ckeditor/start.js',
        ]

        css = {
            'ckeditor': ('/static/admin/js/ckeditor/contents.css',),
        }
