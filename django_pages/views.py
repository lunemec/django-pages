# -*- encoding: utf-8 -*-

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
from django_pages.metadata import get_metadata
from django_pages.pages import get_page, get_index_page, get_post, get_paginated_posts
from django_pages.pages.models import Page
from django_pages.site import get_site
from django_pages.settings import TEMPLATE_PATH


def parse_url(url):
    '''
    parses url format is:
        language/page~pagenum/~post

        example:
            en/my-page-with-something-interresting~5/~post-on-page-5

    @param url: string
    @return dict
    '''

    urlpattern = re.compile(r'''
                          ^                                         # beginning of string
                          ((?P<country_code>[A-z]{2,3})/){0,1}      # country_code match - any 2 or 3 chars, zero or one times
                          (?P<page>[A-z0-9-._]{4,}){0,1}            # page url
                          (~(?P<page_num>\d*)){0,1}                 # ~page number
                          (/~(?P<post>[A-z0-9-._]*)){0,1}           # /~post title
                          $                                         # end of string
                          ''', re.VERBOSE)

    urlmatch = re.match(urlpattern, url)

    if not urlmatch:

        raise Http404

    return urlmatch.groupdict()


@cache_page(10)
def main_view(request, url, test=False):

    url_result = parse_url(url)

    current_site = get_site()

    language = get_language(url_result)

    if not url_result['page']:

        page = get_index_page(language)

    else:

        page = get_page(url_result['page'], language)

    menuitems = page.link.lang.menuitem_set.select_related('page').filter(page__active=True).order_by('position').all()

    for menuitem in menuitems:

        menuitem.current = menuitem.is_current(url_result['page'])

    meta_data = get_metadata(page)

    page_num = url_result['page_num'] or 1

    if url_result['post']:

        posts = get_post(page, url_result['post'])

        template_page = 'wysiwyg_post.html'

        if request.method == 'POST':

            form = handle_comment(request, posts, url)

            set_humanity_check(request)
            form.humanity = translate_humanity(request)

        else:

            form = CommentForm()

            set_humanity_check(request)
            form.humanity = translate_humanity(request)

    else:

        posts = get_paginated_posts(page, page_num)

        template_page = 'wysiwyg_page.html'

    site_content = {'site': current_site,
                    'languages': get_languages(),
                    'current_language': language,
                    'menuitems': menuitems,
                    'page': page,
                    'metadata': meta_data,
                    'posts': posts, }

    try:

        site_content['form'] = form

    except NameError:

        pass

    template = '%s/%s' % (TEMPLATE_PATH, template_page)

    return render_to_response(template, {'site_content': site_content}, context_instance=RequestContext(request))


@cache_page(60 * 60 * 24)
def robots(request):

    site = get_site()
    domain = site.domain

    data = '''Sitemap: http://%s/sitemap.xml
User-agent: *
Disallow: /admin/
Disallow: /media/
Disallow: /static/
''' % domain

    return HttpResponse(data, content_type='text/plain')


@cache_page(60 * 60 * 24)
def generate_sitemap(request):

    data = []

    site_url = 'http://%s/' % get_site().domain

    for language in Language.objects.all():

        for page in Page.objects.filter(link__lang=language):

            page_url = '%s%s/%s' % (site_url, language.country_code, page.link.url)

            data.append(page_url)

            for post in page.post_set.all():

                data.append('%s/~%s' % (page_url, slugify(post.title)))

    return render_to_response('%s/sitemap.xml' % TEMPLATE_PATH, {'urls': data}, context_instance=RequestContext(request))
