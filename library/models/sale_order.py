from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super().onchange_partner_id
        if self.partner_id:
            self.client_order_ref = self.partner_id.vat
        return res
