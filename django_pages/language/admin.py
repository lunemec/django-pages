# -*- encoding: utf-8 -*-

from django import forms

import reversion

from ..common.admin_actions import activate, deactivate
from .models import Language


class LanguageAdminForm(forms.ModelForm):

    country_code = forms.RegexField(r'^[A-z]{2,3}$', error_messages={'invalid': '2-3 letter combination required'})

    class Meta:

        model = Language


class LanguageAdmin(reversion.VersionAdmin):

    form = LanguageAdminForm
    fields = (('language', 'country_code'), 'flag', 'default', 'active')
    list_display = ('language', 'country_code', 'default', 'active')
    list_filter = ('active',)
    actions = [activate, deactivate]
