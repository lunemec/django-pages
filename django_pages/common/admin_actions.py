# -*- encoding: utf-8 -*-


def activate(modeladmin, request, queryset):

    queryset.update(active=True)

activate.short_description = 'Activate selected items.'


def deactivate(modeladmin, request, queryset):

    queryset.update(active=False)

deactivate.short_description = 'Deactivate selected items.'
