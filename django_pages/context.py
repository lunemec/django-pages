# -*- encoding: utf-8 -*-

from .language import get_language, get_languages
from .menu import get_main_menuitems, has_other_menu, get_other_menuitems
from .metadata import get_metadata
from .pages import get_index_page
from .site import get_site, get_scripts


def pages(request):
    """
    Context processor that adds
    all necessary objects to the template
    dict
    """
    current_site = get_site()

    language = get_language({'country_code': ''})
    page = get_index_page(language)

    menuitems = get_main_menuitems('', page)

    meta_data = get_metadata(page)
    scripts = get_scripts()

    site_content = {
        'site': current_site,
        'languages': get_languages(),
        'current_language': language,
        'menuitems': menuitems,
        'page': page,
        'scripts': scripts,
        'metadata': meta_data,
    }

    if has_other_menu():
        site_content['other_menuitems'] = get_other_menuitems()

    return {'site_content': site_content}
