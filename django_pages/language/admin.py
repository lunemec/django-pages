# -*- encoding: utf-8 -*-

from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from ..common.admin_actions import activate, deactivate
from .models import Language


class LanguageAdminForm(forms.ModelForm):
    country_code = forms.RegexField(
        r'^[A-z]{2,3}$',
        label=_('Country code'),
        help_text=_('(US, UK, CZ, SK, ...)'),
        error_messages={
            'invalid': _('2-3 letter combination required (US, UK, CZ, ...)')
        }
    )

    class Meta:
        fields = '__all__'
        model = Language


class LanguageAdmin(admin.ModelAdmin):

    form = LanguageAdminForm
    fields = (('language', 'country_code'), 'flag', 'default', 'active')
    list_display = ('language', 'country_code', 'default', 'active')
    list_filter = ('active',)
    actions = [activate, deactivate]
