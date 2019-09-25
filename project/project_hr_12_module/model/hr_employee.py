from odoo import models, fields, api
from datetime import datetime


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    job_history_ids = fields.One2many(
        comodel_name="hr.job.history",
        string="Job History",
        inverse_name="employee_id")

    allowance_amount = fields.Float(
        string="Allowance Amount")

# Cach 1 :
    # @api.model
    # def create(self, vals):
    #     res = super(HrEmployee, self).create(vals)
    #     vals.update({})
    #     self.prepare_job_history(res.id, res.job_id.id)
    #     return res

    # @api.multi
    # def write(self, vals):
    #     vals_job_id = vals.get('job_id', False)
    #     for employee in self:
    #         if vals_job_id:
    #             employee.prepare_job_history(employee.id, vals_job_id)
    #     return super(HrEmployee, self).write(vals)

    # def prepare_job_history(self, employee_id, job_id):
    #     job_history_env = self.env['hr.job.history']
    #     job_history_env.create({
    #         'employee_id': employee_id,
    #         'job_id': job_id,
    #         'effective_date': datetime.now(),
    #     })

    # Cach 2: 
    # @api.model
    # def create(self, vals):
    #     vals.update({
    #         'job_history_ids': [(
    #             0, False,
    #             {
    #                 'job_id': vals.id,
    #                 'effective_date': datetime.now()
    #             }
    #         )]
    #     })
    #     return super(HrEmployee, self).create(vals)

    # @api.multi
    # def write(self, vals):

    #     vals_job_id = vals.get('job_id', False)

    #     if vals_job_id:
    #         vals['job_history_ids'] = [(
    #             0, False,
    #             {
    #                 'job_id': vals_job_id,
    #                 'effective_date': datetime.utcnow().date(),
    #             }
    #         )]

    #     res = super(HrEmployee, self).write(vals)
    #     return res

    @api.model
    def create(self, vals):

        vals_job_id = vals.get('job_id', False)

        if vals_job_id:
            vals['job_history_ids'] = [(
                0, False,
                {
                    'job_id': vals_job_id,
                    'effective_date': datetime.utcnow().date(),
                }
            )]

        res = super(HrEmployee, self).create(vals)
        return res

    @api.multi
    def write(self, vals):

        vals_job_id = vals.get('job_id', False)

        if vals_job_id:
            vals['job_history_ids'] = [(
                0, False,
                {
                    'job_id': vals_job_id,
                    'effective_date': datetime.utcnow().date(),
                }
            )]

        res = super(HrEmployee, self).write(vals)
        return res

    @api.onchange('km_home_work')
    def onchange_km_home_work(self):
        gas_allowance_env = self.env['hr.gas.allowance']
        domain = [
            ('from_km', '<=', self.km_home_work),
            ('to_km', '>=', self.km_home_work)]
        if self.km_home_work:
            gas_allowances = gas_allowance_env.search(domain)
            self.allowance_amount = gas_allowances.allowance_amount
