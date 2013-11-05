# -*- encoding: utf-8 -*-

from django import forms

from .validators import validate_empty


class CommentForm(forms.Form):

    user = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    comment = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'input-xlarge'}))

    # this is dummy field to fool bots, it is hidden with CSS, if it is filled,
    # it is a bot
    email = forms.CharField(max_length=100, required=False, validators=[validate_empty])

    # this is also for spam protection, but is supposed to be filled with JS
    # required False is because we don't want django's field is required alert
    fillmeup = forms.CharField(max_length=100, required=False)

    one = forms.BooleanField(required=False)
    two = forms.BooleanField(required=False)
    three = forms.BooleanField(required=False)
    four = forms.BooleanField(required=False)
