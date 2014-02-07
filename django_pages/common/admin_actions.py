# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

"""
Common admin actions importable from any module
"""


def activate(modeladmin, request, queryset):
    queryset.update(active=True)

activate.short_description = _('Activate selected items.')


def deactivate(modeladmin, request, queryset):
    queryset.update(active=False)

deactivate.short_description = _('Deactivate selected items.')


def enable_comments(modeladmin, request, queryset):
    queryset.update(comments=True)

enable_comments.short_description = _('Enable comments.')


def disable_comments(modeladmin, request, queryset):
    queryset.update(comments=False)

disable_comments.short_description = _('Disable comments.')
