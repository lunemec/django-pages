# -*- encoding: utf-8 -*-

from django.contrib import admin

from django_pages.comments.models import Comment
from django_pages.feed.models import FeedSettings
from django_pages.language.models import Language
from django_pages.menu.models import MenuItem
from django_pages.metadata.models import MetaSet, MetaData
from django_pages.pages.models import Page, Post
from django_pages.site.models import Site

from django_pages.comments.admin import CommentAdmin
from django_pages.feed.admin import FeedAdmin
from django_pages.language.admin import LanguageAdmin
from django_pages.menu.admin import MenuItemAdmin
from django_pages.metadata.admin import MetaSetAdmin, MetaDataAdmin
from django_pages.pages.admin import PageAdmin, PostAdmin
from django_pages.site.admin import SiteAdmin

admin.site.register(Comment, CommentAdmin)
admin.site.register(FeedSettings, FeedAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MetaSet, MetaSetAdmin)
admin.site.register(MetaData, MetaDataAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Site, SiteAdmin)
