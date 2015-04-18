# -*- encoding: utf-8 -*-

from django.http import Http404

from ..common.errors import ConfigurationError
from .models import Language


def get_language(url_data):
    """
    checks for language in data from url parsing

    @param url_data: dict
    @return Language object
    """
    if not url_data['country_code']:
        language = Language.objects.get(default=True)

        if not language.active:
            raise ConfigurationError('There is no default language active, please activate it in admin')

    else:
        try:
            language = Language.objects.get(country_code=url_data['country_code'])

        except Language.DoesNotExist:
            raise Http404

    return language


def get_languages():
    """
    returns Language QuerySet or ()
    """
    languages = list(Language.objects.filter(active=True))

    if len(languages) > 1:
        return languages

    return tuple()
