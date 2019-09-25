from odoo import models, fields


class HrJobHistory(models.Model):
    _name = "hr.job.history"
    _description = "Hr Job History"

    employee_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Employee")

    job_id = fields.Many2one(
        comodel_name="hr.job",
        string="Job")

    effective_date = fields.Date(
        string="Effective Date")
