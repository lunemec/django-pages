# -*- encoding: utf-8 -*-

import logging


class RequestLog(object):

    def process_request(self, request):
        """
        Log middleware that puts all REQUEST data into one line for each REQUEST

        @param request: HTTP request
        """
        log = logging.getLogger('requestlog')
        log.info('REQUEST: %s' % unicode(request).replace('\n', ' ').encode('utf-8'))
