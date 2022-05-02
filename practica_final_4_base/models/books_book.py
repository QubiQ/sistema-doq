from odoo import api, fields, models
# Importamos libreria para mostrar errores
from odoo.exceptions import UserError


class BooksGenre(models.Model):
    _name = 'books.book'
    _description = 'Books'

    name = fields.Char(required=True)
    price = fields.Float()
    # ISBN
    barcode = fields.Char(string='ISBN')
    edition = fields.Integer()
    book_type = fields.Selection(
        selection=[('fisico', 'Fisico'), ('digital', 'Digital')])
    website = fields.Char()
    date = fields.Date(string='Purchase Date')
    author_id = fields.Many2one(comodel_name='books.author')
    genre_ids = fields.Many2many(comodel_name='books.genre',
                                 string="Genres")

    dealer_line_ids = fields.One2many(
        comodel_name='books.dealer.line',
        inverse_name='book_id', string='Dealers')
    editorial_line_ids = fields.One2many(
        comodel_name='books.editorial.line',
        inverse_name='book_id', string='Editorial')
