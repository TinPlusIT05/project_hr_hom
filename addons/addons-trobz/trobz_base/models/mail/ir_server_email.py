# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

import logging

from odoo import api, models, tools

_logger = logging.getLogger(__name__)


class IrMailServer(models.Model):
    _inherit = 'ir.mail_server'

    @api.model
    def build_email(self, email_from, email_to, subject, body, email_cc=None,
                    email_bcc=None, reply_to=False, attachments=None,
                    message_id=None, references=None, object_id=False,
                    subtype='plain', headers=None, body_alternative=None,
                    subtype_alternative='plain'):
        is_production_instance = tools.config.get(
            'is_production_instance', False)
        if not is_production_instance:
            _logger.warning('Removing email_cc %s', email_cc)
            _logger.warning('Removing email_bcc %s', email_bcc)
            email_cc = None
            email_bcc = None

        msg = super(IrMailServer, self).build_email(
            email_from, email_to, subject, body,
            email_cc=email_cc, email_bcc=email_bcc, reply_to=reply_to,
            attachments=attachments, message_id=message_id,
            references=references, object_id=object_id, subtype=subtype,
            headers=headers, body_alternative=body_alternative,
            subtype_alternative=subtype_alternative)
        return msg
