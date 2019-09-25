# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

import pytz

from odoo import api, fields, models


@api.model
def _tz_get(self):
    # put POSIX 'Etc/*' entries at the end to avoid confusing users -
    # see bug 1086728
    return [(tz, tz) for tz in sorted(pytz.all_timezones, key=lambda tz: tz
                                      if not tz.startswith('Etc/') else '_')]


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _get_default_timezone(self):
        """
        Get default timezone for a user
        """
        configure_parameter_env = self.env['ir.config_parameter']
        return self._context.get('tz') or \
            configure_parameter_env.get_param('Default Timezone',
                                              False)

    tz = fields.Selection(
        _tz_get, string='Timezone',
        default=_get_default_timezone,
        help="The partner's timezone, "
             "used to output proper date and time values "
             "inside printed reports. "
             "It is important to set a value for this field. "
             "You should use the same timezone that is otherwise used to "
             "pick and render date and time values: your computer's timezone."
    )
