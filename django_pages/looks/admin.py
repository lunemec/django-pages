# -*- encoding: utf-8 -*-

from django.contrib import admin

from ..common.admin_actions import activate, deactivate


class LooksAdmin(admin.ModelAdmin):

    fields = ('template', 'posts_per_page', 'active')
    list_display = fields
    actions = [activate, deactivate]
