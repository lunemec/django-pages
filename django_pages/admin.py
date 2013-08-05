# -*- encoding: utf-8 -*-

"""
This file just imports admins from all packages so Django finds them
"""

from django.contrib import admin

from .comments.models import Comment
from .feed.models import FeedSettings
from .language.models import Language
from .looks.models import Template
from .menu.models import MenuItem
from .metadata.models import MetaSet, MetaData
from .pages.models import Page, Post
from .site.models import Site

from .comments.admin import CommentAdmin
from .feed.admin import FeedAdmin
from .language.admin import LanguageAdmin
from .looks.admin import LooksAdmin
from .menu.admin import MenuItemAdmin
from .metadata.admin import MetaSetAdmin, MetaDataAdmin
from .pages.admin import PageAdmin, PostAdmin
from .site.admin import SiteAdmin

admin.site.register(Comment, CommentAdmin)
admin.site.register(FeedSettings, FeedAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Template, LooksAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MetaSet, MetaSetAdmin)
admin.site.register(MetaData, MetaDataAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Site, SiteAdmin)
