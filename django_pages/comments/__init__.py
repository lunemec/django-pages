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
    sets session['humanity'] to dictionary {0: True/False, 1: True/False, .. 3: True/False}

    @param request: Http Request
    @return None
    """
    result = {}

    # this ensures we don't have empty checkboxes
    while result == {} or result == {0: False, 1: False, 2: False, 3: False}:
        for i in xrange(4):
            if random.randint(0, 1):
                result[i] = True

            else:
                result[i] = False

    request.session['humanity'] = result

    # also fill the random number into session
    # this number will be filled into form using JS
    request.session['random_number'] = str(random.random())
    print request.session['random_number']


def translate_humanity(request):
    """
    translates request.session['humanity'] dictionary {0: True, 1: False, ..}
    into 'One, Two, Three' according to numbers that are True

    @param request: Http Request
    @return string
    """
    numbers = []
    translation = {0: 'one', 1: 'two', 2: 'three', 3: 'four'}

    for i in request.session['humanity']:

        if request.session['humanity'][i]:
            numbers.append(translation[i])

    check_string = ', '.join(numbers)

    return check_string


def is_human(request, data):
    if request.session['humanity'] == data:
        return True

    return False


def handle_comment(request, post):
    """
    handles comment and either saves it or displays error

    @param request: Http Request
    @param post: Post object
    @return None or errorfrom django.utils.timezone import make_aware, get_current_timezone
    """
    form = CommentForm(request.POST)
    ip = get_client_ip(request)

    if form.is_valid():
        user = strip_tags(form.cleaned_data['user'])
        comment = strip_tags(form.cleaned_data['comment'])

        one = form.cleaned_data['one']
        two = form.cleaned_data['two']
        three = form.cleaned_data['three']
        four = form.cleaned_data['four']

        random_number = form.cleaned_data['fillmeup']

        if random_number != request.session['random_number']:
            form.spam = 'Please check that you have JavaScript enabled.'
            return form

        if is_human(request, {0: one, 1: two, 2: three, 3: four}):
            # check for duplicate comments
            if Comment.objects.filter(post=post, user=user, comment=comment):
                return CommentForm()

            comment = Comment(post=post, user=user, comment=comment, ip=ip)
            comment.save()

            return CommentForm()

        else:
            form.spam = 'Wrong antispam check'
            return form

    else:
        return form
