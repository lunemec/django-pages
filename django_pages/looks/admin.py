# -*- encoding: utf-8 -*-

import reversion

from ..common.admin_actions import activate, deactivate

class LooksAdmin(reversion.VersionAdmin):

    fields = ('template', 'posts_per_page', 'active')
    list_display = fields
    actions = [activate, deactivate]
