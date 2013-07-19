# -*- encoding: utf-8 -*-

import string

from django import forms
from django.conf.urls import patterns
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

import reversion

from django_pages.menu.models import MenuItem
from django_pages.settings import ADMIN_MEDIA_PREFIX


class MenuItemInline(admin.TabularInline):

    model = MenuItem


class MenuItemUrlField(forms.CharField):

    def validate(self, value):

        super(MenuItemUrlField, self).validate(value)

        allowed = '%s%s%s' % (string.ascii_letters, string.digits, '-._')

        for letter in value:

            if letter not in allowed:

                raise forms.ValidationError(u'These characters are allowed: %s' % allowed)


class MenuItemAdminForm(forms.ModelForm):

    url = MenuItemUrlField('Url', min_length=4)

    class Meta:

        model = MenuItem


class MenuItemAdmin(reversion.VersionAdmin):

    form = MenuItemAdminForm
    fields = (('lang', 'menuitem_name'), 'url')
    list_display = ('menuitem_name', 'lang', 'url', 'move', 'position')

    def move(sefl, obj):
        '''
        Returns html with links to move_up and move_down views.
        '''

        button = u'<a href="%s"><img src="%simg/arrow-%s.png" /> %s</a>'
        prefix = ADMIN_MEDIA_PREFIX

        link = '%d/move_up/' % obj.pk
        html = button % (link, prefix, 'up', _('up')) + " | "
        link = '%d/move_down/' % obj.pk
        html += button % (link, prefix, 'down', _('down'))
        return html

    move.allow_tags = True
    move.short_description = ugettext_lazy('Move')

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

        return redirect('/admin/menu/menuitem/?o=2.-5')

    def move_down(self, request, item_pk):

        if self.has_change_permission(request):

            item = get_object_or_404(MenuItem, pk=item_pk)

            item.decrease_position()

        else:

            raise PermissionDenied

        return redirect('/admin/menu/menuitem/?o=2.-5')
