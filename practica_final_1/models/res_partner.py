from odoo import api, fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # 1º Historia de Usuario
    is_commercial = fields.Boolean(string='Commercial')
    commercial_code = fields.Char(copy=False)
    commission = fields.Float(string='% Commission')

    # 2º Historia de Usuario
    _sql_constraints = [
        ('commercial_code_uniq', 'unique (commercial_code)',
         'The commercial code must be unique!')
    ]

    def unlink(self):
        # Mapped itera sobre un recordset para agrupar un campo en una lista
        if any(self.mapped('commercial_code')):
            raise UserError("You can not delete a contact with"
                            " a Commercial Code")
        # Es lo mismo que hacer
        # for rec in self:
        #     if rec.commercial_code:
        #         raise
        res = super().unlink()

        return res
