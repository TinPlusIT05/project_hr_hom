from odoo import api, models, fields


class HrContract(models.Model):
    _inherit = 'hr.contract'

    coach_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Coach")

    @api.model
    def create(self, vals):
        res = super(HrContract, self).create(vals)
        self.update_coach_id(res.employee_id, res.coach_id)
        return res

    @api.multi
    def write(self, vals):
        res = super(HrContract, self).write(vals)
        self._cr.commit()
        for contract in self:
            contract.update_coach_id(
                contract.employee_id,
                vals.get('coach_id'))
        return res

    def update_coach_id(self, employee_id, coach_id):
        if employee_id:
            employee_id.coach_id = coach_id
