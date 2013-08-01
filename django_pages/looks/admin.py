# -*- encoding: utf-8 -*-

import reversion


class LooksAdmin(reversion.VersionAdmin):

    fields = ('template', 'active')
    list_display = fields
