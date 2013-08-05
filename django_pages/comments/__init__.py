# -*- encoding: utf-8 -*-

import random

from django.utils.html import strip_tags

from .forms import CommentForm
from .models import Comment


def get_client_ip(request):
    """
    Returns requester's IP address from HTTP request

    @param request: Http Request
    @return string
    """

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:

        ip = x_forwarded_for.split(',')[0]

    else:

        ip = request.META.get('REMOTE_ADDR')

    return ip


def set_humanity_check(request):
    """
    sets session['humanity'] to dictionary {0: True/False, 1:True/False, .. 3:True/False}

    @param request: Http Request
    @return None
    """

    result = {}

    for i in xrange(4):

        if random.randint(0, 1):

            result[i] = True

        else:

            result[i] = False

    request.session['humanity'] = result


def translate_humanity(request):
    """
    translates request.session['humanity'] dictionary {0:True, 1:False, ..}
    into 'One, Two, Three' according to numbers that are True

    @param request: Http Request
    @return string
    """

    text = []

    for i in xrange(4):

        if request.session['humanity'][i]:

            if i == 0:
                text.append('one')

            elif i == 1:
                text.append('two')

            elif i == 2:
                text.append('three')

            elif i == 3:
                text.append('four')

        elif request.session['humanity'][i] == {0: False, 1: False, 2: False, 3: False}:

            text.append('None')

    return ', '.join(text)


def is_human(request, data):

    if request.session['humanity'] == data:

        return True

    return False


def handle_comment(request, post):
    '''
    handles comment and either saves it or displays error

    @param request: Http Request
    @param post: Post object
    @return None or errorfrom django.utils.timezone import make_aware, get_current_timezone
    '''

    form = CommentForm(request.POST)
    ip = get_client_ip(request)

    if form.is_valid():

        user = strip_tags(form.cleaned_data['user'])
        comment = strip_tags(form.cleaned_data['comment'])

        one = form.cleaned_data['one']
        two = form.cleaned_data['two']
        three = form.cleaned_data['three']
        four = form.cleaned_data['four']

        if is_human(request, {0: one, 1: two, 2: three, 3: four}):

            if Comment.objects.filter(post=post, user=user, comment=comment):

                return CommentForm()

            comment = Comment(post=post, user=user, comment=comment, ip=ip)
            comment.save()

            return CommentForm()

        else:

            form.spam = 'wrong antispam check'
            return form

    else:

        return form
