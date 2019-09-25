# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

import logging

from odoo import api, models, tools

_logger = logging.getLogger(__name__)


class PostObjectTrobzReport(models.TransientModel):
    _name = 'post.object.trobz.report'
    _description = 'trobz_base > Post Object Report'

    @api.model
    def start(self):
        _logger.info("Trobz_report_base post_object: START")
        self.update_value_report_url()
        _logger.info("Trobz_report_base post_object: END")
        return True

    @api.model
    def update_value_report_url(self):
        interface = tools.config.get('xmlrpc_interface', False)
        port = tools.config.get('xmlrpc_port', False)
        ir_config_para = self.env['ir.config_parameter']
        if interface and port:
            values = 'http://%s:%s' % (interface, str(port))
            ir_config_para.set_param('report.url', values)
        else:
            web_local = ir_config_para.get_param(key='web.base.url')
            ir_config_para.set_param('report.url', web_local)
        return True
