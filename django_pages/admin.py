# -*- encoding: utf-8 -*-

"""
This file just imports admins from all packages so Django finds them
"""

from django.contrib import admin

from django_pages.comments.models import Comment
from django_pages.feed.models import FeedSettings
from django_pages.language.models import Language
from django_pages.looks.models import Template
from django_pages.menu.models import Menu, MenuItem
from django_pages.metadata.models import MetaSet, MetaData
from django_pages.pages.models import Page, Post
from django_pages.site.models import Site, Script

from django_pages.comments.admin import CommentAdmin
from django_pages.feed.admin import FeedAdmin
from django_pages.language.admin import LanguageAdmin
from django_pages.looks.admin import LooksAdmin
from django_pages.menu.admin import MenuAdmin, MenuItemAdmin
from django_pages.metadata.admin import MetaSetAdmin, MetaDataAdmin
from django_pages.pages.admin import PageAdmin, PostAdmin
from django_pages.site.admin import SiteAdmin, ScriptAdmin

admin.site.register(Comment, CommentAdmin)
admin.site.register(FeedSettings, FeedAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Template, LooksAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MetaSet, MetaSetAdmin)
admin.site.register(MetaData, MetaDataAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Script, ScriptAdmin)
