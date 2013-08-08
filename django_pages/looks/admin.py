# -*- encoding: utf-8 -*-

import reversion


class LooksAdmin(reversion.VersionAdmin):

    fields = ('template', 'posts_per_page', 'active')
    list_display = fields
