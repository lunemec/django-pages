#! -*- encoding: utf-8 -*-

from django.core.exceptions import ValidationError


def validate_empty(value):
    """ Validates that field is empty
    This is a protection against spam bots
    the field is supposed to be empty because
    it is hidden by CSS from the user """

    if value:
        raise ValidationError(u'Email must not be filled, you are a SPAM BOT!')
