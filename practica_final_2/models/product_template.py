from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    # 1º Historia de Usuario
    component_line_ids = fields.One2many(
        comodel_name='product.pack.line',
        inverse_name='pack_id',
        string='Pack Components Lines')
    is_pack = fields.Boolean(string='Is Pack')

    # 2º Historia de Usuario
    price_pack_method = fields.Selection(
        string='Cost Calculation',
        selection=[('normal_price', 'Normal Price'),
                   ('component_total', 'Sum Components')],
        default="normal_price")

    list_price = fields.Float(
        compute="_compute_price_pack",
        store=True,
        readonly=False,
        )

    @api.depends('price_pack_method', 'component_line_ids')
    def _compute_price_pack(self):
        for rec in self:
            if rec.price_pack_method == 'component_total':
                rec.list_price = 0
                for line in rec.component_line_ids:
                    rec.list_price += line.quantity * line.price
            else:
                rec.list_price = rec.list_price or 0
