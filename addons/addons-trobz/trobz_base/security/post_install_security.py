# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import api, models

group_configure_user = 'Administration / User'


class PostInstallSecurity(models.TransientModel):
    _name = 'post.install.security.trobz.base.module'
    _description = 'Post Install Security for Trobz Base Module'

    @api.model
    def create_model_access_rights(self):
        MODEL_ACCESS_RIGHTS = {
            ('res.users'): {
                (group_configure_user): [1, 1, 1, 1],
            },
            ('ir.module.category'): {
                (group_configure_user): [1, 0, 0, 0],
            },
            ('ir.module.module'): {
                (group_configure_user): [1, 0, 0, 0],
            },
            ('ir.module.module.dependency'): {
                (group_configure_user): [1, 0, 0, 0],
            }
        }
        self.env['access.right.generator'].with_context(
            module_name='trobz.base').create_model_access_rights(
            MODEL_ACCESS_RIGHTS)
        return True

    @api.model
    def start(self):
        self.create_model_access_rights()
