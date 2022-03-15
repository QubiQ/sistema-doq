from odoo import fields, models


class BooksGenre(models.Model):
    _name = 'books.book'
    _description = 'Books'

    # Nombre del libro - char
    name = fields.Char(required=True)
    # Precio - float
    price = fields.Float(string="Price")
    # Edición - int
    edition = fields.Integer(string="Edition")
    # Fisico o Digital - Selección
    book_type = fields.Selection(
        string="Type",
        selection=[('fisico', 'Fisico'), ('digital', 'Digital')])
    # Website - char
    website = fields.Char(string="Website")
    # Comprado/No comprado - bool
    available = fields.Boolean(string="Available")
    # Fecha de compra - Date
    date = fields.Date(string='Purchase Date')
    # Los campos que se piden en los casos de usuario 2 y 4
    author_id = fields.Many2one(string="Author", comodel_name='books.author')
    genre_ids = fields.Many2many(comodel_name='books.genre', string="Genres")
