# -*- encoding: utf-8 -*-

from django.contrib import admin

from ..common.admin_actions import activate, deactivate


class LooksAdmin(admin.ModelAdmin):

    fields = ('template', 'submenu_max_characters', 'active')
    list_display = fields
    actions = [activate, deactivate]
