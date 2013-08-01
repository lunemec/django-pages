# -*- encoding: utf-8 -*-

import logging


class RequestLog(object):

    def process_request(self, request):

        log = logging.getLogger('requestlog')
        log.info('REQUEST: %s' % unicode(request).replace('\n', ' ').encode('utf-8'))
