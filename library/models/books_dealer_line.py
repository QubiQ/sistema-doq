from odoo import api, fields, models


class BooksDealerLine(models.Model):
    _name = 'books.dealer.line'
    _description = 'New Description'

    dealer_id = fields.Many2one(comodel_name='res.partner', string="Dealer")
    price_unit = fields.Float(string='Price Unit')
    sale_unit = fields.Integer(string='Unit Sales')
    book_id = fields.Many2one(comodel_name='books.book', string="Book")
