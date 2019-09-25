# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    @api.multi
    def button_upgrade(self):
        """
        Overwrite this function to upgrade all installed modules from Trobz
        when upgrading the module "trobz_base"
        """
        _logger.info("Trobz_button_upgrade is proccessing.........")
        upgrade_ids = self.ids
        # check whether "trobz_base" is in the list
        check_trobz_base = self.search([('name', '=', 'trobz_base'),
                                        ('id', 'in', upgrade_ids)])
        if check_trobz_base:
            # get all installed module with author "Trobz"
            installed_trobz_modules = self.search([('state', '=', 'installed'),
                                                   ('author', '=', 'Trobz')])
            upgrade_ids.extend(installed_trobz_modules.ids)
            """
            uniquifying the ids to avoid:
                Error: "One of the records you are trying to modify has
                already been deleted (Document type: %s)"
            if exist an duplicate id in ids
            """
            upgrade_ids = list(set(upgrade_ids))
        _logger.info("Trobz_button_upgrade ids of modules "
                     "that need to upgrade: %s" % upgrade_ids)
        _logger.info("Trobz_button_upgrade super  "
                     "native button_upgrade...")
        # call super
        upgrade_modules = self.browse(upgrade_ids)
        super(IrModuleModule, upgrade_modules).button_upgrade()
