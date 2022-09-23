from odoo import models,fields,api
from odoo.exceptions import ValidationError


class PideClaveWizard(models.TransientModel):
    _name = 'seg.pide.clave.wizard'
    _description = 'Pide Clave'

    seg_clave = fields.Char(string='Contraseña')
    seg_operacion = fields.Char(string='Tipo Operacion')


    def action_clave_cancela(self):
        movimiento = self.env['account.move'].search([('id', '=', self.env.context['active_id'])])[0]
        clave = self.env['seg.res.partner.ops'].search([('seg_res_partner_id', '=', movimiento.env.company.id),
                                                        ('seg_journal_id', '=', movimiento.journal_id.id),
                                                        ('seg_operacion', '=', 'CA')])
        if self.seg_clave != clave.seg_clave:
            raise ValidationError('Contraseña Incorrecta')
        else:
            vals = { 'seg_validado' : True }
            movimiento.write(vals)
            res = movimiento.button_cancel()
        return res

    def action_clave_borrador(self):
        movimiento = self.env['account.move'].search([('id', '=', self.env.context['active_id'])])[0]
        clave = self.env['seg.res.partner.ops'].search([('seg_res_partner_id', '=', movimiento.env.company.id),
                                                        ('seg_journal_id', '=', movimiento.journal_id.id),
                                                        ('seg_operacion', '=', 'RB')])
        if self.seg_clave != clave.seg_clave:
            raise ValidationError('Contraseña Incorrecta')
        else:
            vals = { 'seg_validado' : True }
            movimiento.write(vals)
            res = movimiento.button_draft()
        return res

    # def action_clave_publica(self):
    #     movimiento = self.env['account.move'].search([('id', '=', self.env.context['active_id'])])[0]
    #     clave = self.env['seg.res.partner.ops'].search([('seg_res_partner_id', '=', movimiento.env.company.id),
    #                                                     ('seg_journal_id', '=', movimiento.journal_id.id),
    #                                                     ('seg_operacion', '=', 'PU')])
    #     if self.seg_clave != clave.seg_clave:
    #         raise ValidationError('Contraseña Incorrecta')
    #     else:
    #         vals = { 'seg_validado' : True }
    #         movimiento.write(vals)
    #         res = movimiento.action_post()
    #     return res


    # def action_clave_ncred(self):
    #     # parametro = self.env.context.get('prueba')
    #     # print(parametro)
    #     movimiento = self.env['account.move'].search([('id', '=', self.env.context['active_id'])])[0]
    #     ncred_journal_id = self.env['account.journal'].search([('seg_ncred', '=', 'Si')])
    #     clave = self.env['seg.res.partner.ops'].search([('seg_res_partner_id', '=', movimiento.env.company.id),
    #                                                     ('seg_journal_id', '=', ncred_journal_id.id),
    #                                                     ('seg_operacion', '=', 'CR')])
    #     if self.seg_clave != clave.seg_clave:
    #         raise ValidationError('Contraseña Incorrecta')
    #     else:
    #         vals = { 'seg_validado' : True }
    #         movimiento.write(vals)
    #         # res = movimiento.action_reverse()
    #         action = self.env["ir.actions.actions"]._for_xml_id("account.action_view_account_move_reversal")
    #
    #         res = action
    #     return res
