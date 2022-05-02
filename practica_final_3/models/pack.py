from attr import field
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    pack_line_ids = fields.One2many(
        comodel_name='line.packs', inverse_name='pack_id')
    is_pack = fields.Boolean()

    type_price = fields.Selection(
        string='Cálculo de precio',
        selection=[('suma_componentes', 'Suma de componentes'),
                   ('precio_normal', 'Precio normal')]
    )

    @api.onchange('type_price')
    def _onchange_price(self):
        for rec in self:
            if rec.is_pack:
                if rec.type_price == 'suma_componentes':
                    rec.list_price = 0
                    for product in rec.pack_line_ids:
                        rec.list_price += product.price


class LinePacks(models.Model):
    _name = 'line.packs'
    _description = 'Module for the packs line'

    pack_id = fields.Many2one(comodel_name='product.template')
    product_id = fields.Many2one(comodel_name='product.template')
    quantity = fields.Integer()
    price = fields.Float()

    @api.onchange('product_id')
    def _onchange_price(self):
        for rec in self:
            rec.price = rec.product_id.list_price

    @api.onchange('quantity')
    def _onchange_price(self):
        for rec in self:
            rec.price = rec.product_id.list_price * rec.quantity


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def product_id_change(self):
        res = super().product_id_change()
        if self.product_id and self.product_id.is_pack and self.product_id.pack_line_ids:
            self.name += ('\n-- Components --')
            for line in self.product_id.pack_line_ids:
                self.name += '\n %s - %i' % (line.product_id.name,
                                             line.quantity)
        return res

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    # Historia de usuario 1
    has_pack = fields.Boolean(string='Has a pack')
    
    # Historia de usuario 2
    pack_id = fields.Many2one(comodel_name='product.template', string='Pack', domain=[('is_pack','=', True)])
    
    # Historia de usuario 3
    @api.onchange('pack_id')
    def on_change_pack_id(self):
        if self.pack_id:
            # Historia de usuario 4
            self.order_line = False
            # Fin de la historia de usuario 4
            productes = self.pack_id.pack_line_ids.product_id
            for producte in productes:
                self.env['sale.order.line'].new({
                    'product_id': producte.id,
                    'order_id': self.id
                })
    
    
    
