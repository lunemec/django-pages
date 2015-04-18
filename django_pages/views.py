# -*- encoding: utf-8 -*-

"""
This module handles all views that django-pages support
"""

import re

from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.text import slugify
from django.views.decorators.cache import cache_page

from django_pages.comments import handle_comment, set_humanity_check, translate_humanity
from django_pages.comments.forms import CommentForm
from django_pages.language import get_language, get_languages
from django_pages.language.models import Language
from django_pages.looks import get_template
from django_pages.menu import get_main_menuitems, has_other_menu, get_other_menuitems
from django_pages.metadata import get_metadata
from django_pages.pages import get_page, get_index_page, get_post, get_paginated_posts
from django_pages.pages.models import Page
from django_pages.site import get_site, get_scripts


def parse_url(url):
    """
    parses url format is:
        language/page~pagenum/~post

        example:
            en/my-page-with-something-interresting~5/~post-on-page-5

    @param url: string
    @return dict
    """
    urlpattern = re.compile(
        r"""
        ^                                         # beginning of string
        ((?P<country_code>[A-z]{2,3})/){0,1}      # country_code match - any 2 or 3 chars
        (?P<page>[A-z0-9-._]{4,}){0,1}            # page url
        (~(?P<page_num>\d*)){0,1}                 # ~page number
        (/~(?P<post>[A-z0-9-._]*)){0,1}           # /~post title
        $                                         # end of string
        """,
        re.VERBOSE
    )

    urlmatch = re.match(urlpattern, url)
    if not urlmatch:
        raise Http404

    return urlmatch.groupdict()


def handle_comment_form(request, user_last_post):
    """
    Handles comment form.
    Prefills the JS random_number check, saves comment or
    shows empty form

    @param request: HTTP request
    @param user_last_post: pages.models.Post instance

    @return comments.form.CommentForm instance
    """
    if request.method == 'POST':
        form = handle_comment(request, user_last_post)

    else:
        form = CommentForm()

    set_humanity_check(request)
    form.humanity = translate_humanity(request)
    form.js_check = request.session['random_number']

    return form


@cache_page(10)
def main_view(request, url, preview=False):
    """
    @param request: HTTP request
    @param url: string
    @param preview: boolean
    """
    url_result = parse_url(url)
    current_site = get_site()

    # sets tuple (template_name, posts_on_page)
    current_template = get_template()
    language = get_language(url_result)

    if not url_result['page']:
        page = get_index_page(language)

    else:
        page = get_page(url_result['page'], language, preview)

    menuitems = get_main_menuitems(url_result['page'], page, preview)
    meta_data = get_metadata(page)
    page_num = url_result['page_num'] or 1

    if url_result['post']:
        posts = get_post(page, url_result['post'], preview)
        template_page = 'post.html'
        form = handle_comment_form(request, posts)

    else:
        posts = get_paginated_posts(page, page_num, page.items_per_menu)
        template_page = 'page.html'

    site_content = {'site': current_site,
                    'languages': get_languages(),
                    'current_language': language,
                    'menuitems': menuitems,
                    'page': page,
                    'scripts': get_scripts(),
                    'metadata': meta_data,
                    'posts': posts, }

    if has_other_menu():
        site_content['other_menuitems'] = get_other_menuitems()

    try:
        site_content['form'] = form

    except NameError:
        pass

    template = '{}/{}'.format(current_template[0], template_page)

    return render_to_response(
        template,
        {'site_content': site_content},
        RequestContext(request)
    )


@cache_page(60 * 60 * 24)
def robots(request):
    """
    generates robots.txt, which pretty much does not change
    """
    site = get_site()
    domain = site.domain

    data = """Sitemap: http://{}/sitemap.xml
User-agent: *
Disallow: /admin/
Disallow: /media/
Disallow: /static/
""".format(domain)

    return HttpResponse(data, content_type='text/plain')


@cache_page(60 * 60 * 24)
def generate_sitemap(request):
    """
    generates /sitemap.xml
    """
    data = []
    site_url = 'http://{}/'.format(get_site().domain)

    for language in Language.objects.all():
        for page in Page.objects.filter(link__lang=language):
            page_url = '{}{}/{}'.format(
                site_url,
                language.country_code,
                page.link.url
            )

            data.append(page_url)

            for post in page.post_set.all():
                data.append('{}/~{}'.format(page_url, slugify(post.title)))

    return render_to_response(
        'sitemap.xml',
        {'urls': data},
        RequestContext(request),
        content_type='application/xml'
    )
