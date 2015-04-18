# -*- encoding: utf-8 -*-

from django.conf.urls import patterns
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _

from django_pages.settings import ADMIN_MEDIA_PREFIX
from .models import MenuItem


class MenuAdmin(admin.ModelAdmin):

    fields = ('name', )
    list_display = ('name', )


class MenuItemAdmin(admin.ModelAdmin):

    fields = (('lang', 'menu', 'menuitem_name'), 'url', 'style')
    list_display = (
        'menuitem_name',
        'lang',
        'menu',
        'url',
        'move',
        'position',
        'style'
    )
    list_filter = ('lang', 'menu')
    prepopulated_fields = {"url": ("menuitem_name",)}

    def move(self, obj):
        """
        Returns html with links to move_up and move_down views.
        """
        button = u'<a href="%s"><img src="%simg/arrow-%s.png" /> %s</a>'
        prefix = ADMIN_MEDIA_PREFIX

        link = '%d/move_up/' % obj.pk
        html = button % (link, prefix, 'up', _('up')) + " | "
        link = '%d/move_down/' % obj.pk
        html += button % (link, prefix, 'down', _('down'))

        return html

    move.allow_tags = True
    move.short_description = _('Move')

    def get_urls(self):
        admin_view = self.admin_site.admin_view
        urls = patterns(
            '',
            (r'^(?P<item_pk>\d+)/move_up/$', admin_view(self.move_up)),
            (r'^(?P<item_pk>\d+)/move_down/$', admin_view(self.move_down)),
        )

        return urls + super(MenuItemAdmin, self).get_urls()

    def move_up(self, request, item_pk):
        if self.has_change_permission(request):
            item = get_object_or_404(MenuItem, pk=item_pk)
            item.increase_position()

        else:
            raise PermissionDenied

        return redirect('/admin/menu/menuitem/?o=2.3.-6.-5')

    def move_down(self, request, item_pk):
        if self.has_change_permission(request):
            item = get_object_or_404(MenuItem, pk=item_pk)
            item.decrease_position()

        else:
            raise PermissionDenied

        return redirect('/admin/menu/menuitem/?o=2.3.-6.-5')
