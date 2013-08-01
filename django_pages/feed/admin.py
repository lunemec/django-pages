# -*- encoding: utf-8 -*-

from django.contrib import admin

from ..common.admin_actions import activate, deactivate


class FeedAdmin(admin.ModelAdmin):

    list_display = ('site_title', 'latest_post_count', 'active')
    actions = [activate, deactivate]
