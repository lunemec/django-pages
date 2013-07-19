import datetime

from django.utils.timezone import make_aware, get_current_timezone

from django_pages.log.models import Log


class RequestLog(object):

    def process_request(self, request):

        now = make_aware(datetime.datetime.now(), get_current_timezone())
        log = Log(when=now, logline=str(request))
        log.save()
