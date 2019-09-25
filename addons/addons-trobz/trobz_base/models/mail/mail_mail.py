# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

import logging

from odoo import api, models, tools


class MailMail(models.Model):
    _inherit = 'mail.mail'

    @api.multi
    def _send_prepare_values(self, partner=None):
        """
        Trobz: Config send mail when is_production_instance is False
        """
        res = super(MailMail, self)._send_prepare_values(partner=partner)
        # Check production instance
        is_production_instance = tools.config.get(
            'is_production_instance', False)
        if not is_production_instance:
            # Get default_email
            default_email = self.env['ir.config_parameter'].get_param(
                'default_email', default='noone@trobz.com')
            logging.warning('Changing the email_to from %s to %s',
                            res['email_to'], default_email)
            res['body'] = "<i>Original recipients: %s</i><br/>" % \
                ','.join(res['email_to']) + res['body']
            res['email_to'] = [default_email]
        return res
