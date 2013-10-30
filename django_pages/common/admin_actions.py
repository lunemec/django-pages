# -*- encoding: utf-8 -*-

"""
Common admin actions importable from any module
"""

def activate(modeladmin, request, queryset):
    queryset.update(active=True)

activate.short_description = 'Activate selected items.'


def deactivate(modeladmin, request, queryset):
    queryset.update(active=False)

deactivate.short_description = 'Deactivate selected items.'

def enable_comments(modeladmin, request, queryset):
    queryset.update(comments=True)

enable_comments.short_description = 'Enable comments.'

def disable_comments(modeladmin, request, queryset):
    queryset.update(comments=False)

disable_comments.short_description = 'Disable comments.'
