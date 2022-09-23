from odoo import api, models, fields


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    seg_ncred = fields.Selection([('No', 'No'), ('Si', 'Si')], default='No', string='Nota de Credito')
