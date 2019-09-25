# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

import logging
from lxml import etree

from odoo import api, models, SUPERUSER_ID
from odoo.osv.orm import setup_modifiers

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def get_company_currency_of_current_user(self):
        """
        Get company currency of current logged in user
        """
        return self.company_id and self.company_id.currency_id or None

    @api.model
    def get_company_partner_id_of_current_user(self):
        """
        Get company partner id from current logged in user
        """
        return self.company_id and self.company_id.partner and\
            self.company_id.partner_id.id or None

    @api.multi
    def _is_admin(self):
        """
        - modify _is_admin function in res.users
        - admin is superuser or has group erp_manager
            or has group configure_user. Normally, General manager will have
            group configure_user
        """
        # only support one object
        self.ensure_one()

        return self.id == SUPERUSER_ID or\
            self.sudo(self).has_group('base.group_erp_manager') or \
            self.sudo(self).has_group('trobz_base.group_configure_user')

    def _trigger_inverse_password(self, vals):
        """
        On module "auth_encrypt", field password use inverse function
        named "_inverse_passord", this function has same name as
        inverse function of field "new_password" in core module
        So, This raises an issue that can't trigger inverse function
        of "new_password" anymore,
        Here we will set value new_password to password. We don't use field
        password because we don't want password of customer will show to users
        """
        new_password = vals.get('new_password', '')
        if new_password:
            for user in self:
                # assign to password to trigger inverse function to compute
                # password_enscrypt
                user.password = new_password

    def write(self, vals):
        self._trigger_inverse_password(vals)

        return super(ResUsers, self).write(vals)

    @api.model
    def fields_view_get(self, view_id=None, view_type='form',
                        toolbar=False, submenu=False):
        res = super(ResUsers, self).fields_view_get(view_id=view_id,
                                                    view_type=view_type,
                                                    toolbar=toolbar,
                                                    submenu=submenu)
        # Only admin users can see password in res_users form
        # see function _is_admin to know who is admin
        if not self.env.user._is_admin():
            doc = etree.fromstring(res['arch'])
            if view_type == 'form':
                for node in doc.xpath("//field"):
                    if node.get('name') == 'new_password':
                        node.set('invisible', '1')
                    setup_modifiers(node)
                for node in doc.xpath("//label"):
                    if node.get('for') == 'new_password':
                        node.set('invisible', '1')
                    setup_modifiers(node)
            res['arch'] = etree.tostring(doc)
        return res
