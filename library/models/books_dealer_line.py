from odoo import api, fields, models


class BooksDealerLine(models.Model):
    _name = 'books.dealer.line'
    _description = 'New Description'
    # CASO DE USUARIO 1
    # Distribuidor relacionado con el modelo contactos
    dealer_id = fields.Many2one(comodel_name='res.partner', string="Dealer")
    price_unit = fields.Float(string='Price Unit')
    sale_unit = fields.Integer(string='Unit Sales')
    # Relacion necesaria para el One2many
    book_id = fields.Many2one(comodel_name='books.book', string="Book")
