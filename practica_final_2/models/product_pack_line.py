# Copyright 2021 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ProductPackLine(models.Model):
    _name = 'product.pack.line'
    # 1º Historia de usuario
    pack_id = fields.Many2one(
        comodel_name='product.template',
        string="Pack",
    )
    component_id = fields.Many2one(
        comodel_name='product.product',
        string="Component",
        required=True,
    )
    quantity = fields.Integer(
        string="Quantity",
    )
    price = fields.Float(
        string="Price",
    )

    @api.onchange('component_id')
    def onchange_component_id(self):
        self.price = self.component_id.list_price
