from odoo import api, models, fields


class account_move(models.Model):
    _inherit = "account.move"

    seg_validado = fields.Boolean(string='Validado', default=False)

    def action_pide_clave_cancela(self):
        action = self.env.ref('iit_segop.action_pide_clave_cancela').read()[0]
        return action

    def action_pide_clave_borrador(self):
        action = self.env.ref('iit_segop.action_pide_clave_borrador').read()[0]
        return action

    # def action_pide_clave_publica(self):
    #     action = self.env.ref('iit_segop.action_pide_clave_publica').read()[0]
    #     return action

    # def action_pide_clave_ncred(self):
    #     # parametro = {'prueba': 'Va el valor'}
    #     # self.env.context.write(parametro)
    #     self.with_context(prueba='Aqui va')
    #     action = self.env.ref('iit_segop.action_pide_clave_ncred').read()[0]
    #     action['domain'] = [('prueba', '=', 'Primer intento')]
    #     return action

    # def action_pide_clave_crear(self):
    #     action = self.env.ref('iit_segop.action_pide_clave_crear')().read()[0]
    #     return action

    @api.model
    def button_cancel(self):
        if not self.seg_validado:
            clave = self.env['seg.res.partner.ops'].search([('seg_res_partner_id', '=', self.env.company.id),
                                                            ('seg_journal_id', '=', self.journal_id.id),
                                                            ('seg_operacion', '=', 'CA')])
            if clave:
                res = self.action_pide_clave_cancela()
            else:
                res = super(account_move, self).button_cancel()
                self.seg_validado = False
        else:
            res = super(account_move, self).button_cancel()
            self.seg_validado = False
        return res

    def button_draft(self):
        if not self.seg_validado:
            clave = self.env['seg.res.partner.ops'].search([('seg_res_partner_id', '=', self.env.company.id),
                                                            ('seg_journal_id', '=', self.journal_id.id),
                                                            ('seg_operacion', '=', 'RB')])
            if clave:
                res = self.action_pide_clave_borrador()
            else:
                res = super(account_move, self).button_draft()
                self.seg_validado = False
        else:
            res = super(account_move, self).button_draft()
            self.seg_validado = False
        return res

    # def action_post(self):
    #     if not self.seg_validado:
    #         clave = self.env['seg.res.partner.ops'].search([('seg_res_partner_id', '=', self.env.company.id),
    #                                                         ('seg_journal_id', '=', self.journal_id.id),
    #                                                         ('seg_operacion', '=', 'PU')])
    #         if clave:
    #             res = self.action_pide_clave_publica()
    #         else:
    #             res = super(account_move, self).action_post()
    #             self.seg_validado = False
    #     else:
    #         res = super(account_move, self).action_post()
    #         self.seg_validado = False
    #     return res


    # def create(self, vals):
    #     if not self.seg_validado:
    #         clave = self.env['seg.res.partner.ops'].search([('seg_res_partner_id', '=', self.env.company.id),
    #                                                         ('seg_journal_id', '=', self.journal_id.id),
    #                                                         ('seg_operacion', '=', 'CR')])
    #         if clave:
    #             res = self.action_pide_clave_crear(vals)
    #         else:
    #             res = super(account_move, self).action_create(vals)
    #             self.seg_validado = False
    #     else:
    #         res = super(account_move, self).action_create(vals)
    #         self.seg_validado = False
    #     return res


    # def action_reverse(self):
    #     if not self.seg_validado:
    #         ncred_journal_id = self.env['account.journal'].search([('seg_ncred', '=', 'Si')])
    #         clave = self.env['seg.res.partner.ops'].search([('seg_res_partner_id', '=', self.env.company.id),
    #                                                         ('seg_journal_id', '=', ncred_journal_id.id),
    #                                                         ('seg_operacion', '=', 'CR')])
    #         if clave:
    #             res = self.action_pide_clave_ncred()
    #         else:
    #             res = super(account_move, self).action_reverse()
    #             self.seg_validado = False
    #     else:
    #         res = super(account_move, self).action_reverse()
    #         self.seg_validado = False
    #     return res