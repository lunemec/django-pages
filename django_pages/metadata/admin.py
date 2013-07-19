# -*- encoding: utf-8 -*-

from django.contrib import admin

import reversion

from django_pages.metadata.models import MetaData


class MetaDataInline(admin.TabularInline):

    model = MetaData


class MetaSetAdmin(reversion.VersionAdmin):

    fields = (('language', 'name'),)
    list_display = ('name', 'language')
    inlines = (MetaDataInline, )


class MetaDataAdmin(reversion.VersionAdmin):

    list_display = ('__unicode__', 'name', 'content')
