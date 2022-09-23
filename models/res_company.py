from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.company'

    seg_ops = fields.One2many(comodel_name='seg.res.partner.ops', inverse_name='seg_res_partner_id')


class ResPartnerOps(models.Model):
    _name = 'seg.res.partner.ops'

    seg_res_partner_id = fields.Many2one(comodel_name='res.company')
    seg_journal_id = fields.Many2one(comodel_name='account.journal', string="Diario", required=True)
    seg_operacion = fields.Selection([('RB','Restablecer a Borrador'),('CA','Cancelar'),('PU','Publicar'),('CR','Crear')],string='Tipo de Operacion',required=True, default='CA')
    seg_clave = fields.Char(string="Clave", required=True)


