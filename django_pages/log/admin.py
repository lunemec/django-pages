# -*- encoding: utf-8 -*-

from django.contrib import admin


class LogAdmin(admin.ModelAdmin):

    list_display = ('when', 'logline')
