from odoo import api, fields, models
from odoo.exceptions import UserError



class ResPartner(models.Model):
    _inherit = 'res.partner'
    # 1º Historia de usuario
    is_library_partner = fields.Boolean(string='Is Library Partner')
    library_partner_code = fields.Char(string='Library Partner Code')
    
    _sql_constraints = [
        ('library_partner_code_unique', 'unique (library_partner_code,company_id)', 'The Library Partner Code of contact must be unique per company !')
    ]
    def singup(self):
        self.write({'is_library_partner': True})

    # 2º Historia de usuario
    def dropout(self):
        self.write({'is_library_partner': False,
                    'library_partner_code': False})
        
    # 6º Historia de Usuario
    def unlink(self):
        for rec in self:
            if rec.is_library_partner:
                if self.env['books.rent'].search(
                    [('partner_id', '=', rec.id),
                     ('state', '=', 'loan')]):
                    raise UserError(
                        "The partner %s still has books to return" % rec.name)
        return super().unlink()
    
    # 7º Historia de Usuario
    def get_books(self):
        # Esto lo hago para asegurarme de este método se lance desde un registro
        # len(self) == 1
        self.ensure_one()
        return self.env['books.rent'].search([('partner_id', '=', self.id),
                                              ('state', '=', 'loan')])
        