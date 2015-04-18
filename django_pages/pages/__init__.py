# -*- encoding: utf-8 -*-

import datetime

from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.utils.text import slugify

from .models import Page
from ..common.errors import ConfigurationError


def get_index_page(language):
    """
    checks for page with index=True and returns it

    @param language: Language object
    @return Page object
    """
    try:
        page = Page.objects.select_related('link', 'metadata_set', 'link__lang').get(index=True, link__lang=language)
        return page

    except Page.DoesNotExist:
        raise ConfigurationError('There is no index Page for this Language, please make sure exactly one Page has index field checked True')

    except Page.MultipleObjectsReturned:
        raise ConfigurationError('There are multiple index Pages for this Language, please make sure only 1 Page has index field checked True')


def get_page(page_url, language, preview=False):
    """
    returns page for specific url

    @param page_url: string
    @param language: Language object
    @return Page object
    """
    try:
        page = Page.objects.select_related('link', 'metadata_set', 'link__lang').get(link__url=page_url, link__lang=language)
        if page.active or preview:
            return page

        else:
            raise Http404

    except Page.DoesNotExist:
        raise Http404


def get_paginated_posts(page, page_num=1, posts_on_page=10):
    """
    returns posts paginated by settings.POSTS_ON_PAGE for page object or ()

    @param page: Page object
    @return Paginator object
    """
    if page.have_posts():
        posts = page.post_set.filter(active=True).order_by('-created')
        posts_visible = [item for item in posts if item.is_visible(datetime.datetime.now())]
        paginated_posts = Paginator(posts_visible, posts_on_page)

        try:
            return paginated_posts.page(page_num)

        except EmptyPage:
            return paginated_posts.page(paginated_posts.num_pages)

    return tuple()


def get_post(page, post_title, preview=False):
    """
    returns post object or 404

    @param page: Page object
    @param post_title: string
    @return Post object
    """
    for post in page.post_set.all():
        if slugify(post.title) == post_title and (post.active or preview):
            return post

    raise Http404
