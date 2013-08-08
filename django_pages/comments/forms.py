# -*- encoding: utf-8 -*-

from django import forms


class CommentForm(forms.Form):

    user = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    comment = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'input-xlarge'}))

    one = forms.BooleanField(required=False)
    two = forms.BooleanField(required=False)
    three = forms.BooleanField(required=False)
    four = forms.BooleanField(required=False)
