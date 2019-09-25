from odoo import api, models, fields


class HrGasAllowance(models.Model):
    _name = "hr.gas.allowance"
    _description = "Hr Gas Allowance"

    name = fields.Char(
        string="Name",
        compute="_compute_name")

    from_km = fields.Float(
        string="From Km")

    to_km = fields.Float(
        string="To Km")

    allowance_amount = fields.Float(
        string="Allowance Amount")

    @api.multi
    def _compute_name(self):
        for gas_allowance in self:
            name = "From " + str(gas_allowance.from_km) + " Km to " + \
                str(gas_allowance.to_km) + " Km"
            gas_allowance.name = name
