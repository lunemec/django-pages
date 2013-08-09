# -*- encoding: utf-8 -*-

from django.contrib import admin

import reversion

from .models import MetaData


class MetaDataInline(admin.TabularInline):

    model = MetaData


class MetaSetAdmin(reversion.VersionAdmin):

    fields = (('language', 'name'),)
    list_display = ('name', 'language')
    inlines = (MetaDataInline, )
    list_filter = ('language', )
    search_fields = ['metadata__name', 'metadata__content']


class MetaDataAdmin(reversion.VersionAdmin):

    list_display = ('__unicode__', 'name', 'content')
    list_filter = ('meta_set__name', 'name')
    search_fields = ['content']
