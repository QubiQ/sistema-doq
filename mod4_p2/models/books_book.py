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
    genre_ids = fields.Many2many(comodel_name='books.genre', string="Genres")
    author_id = fields.Many2one(string="Author", comodel_name='books.author')
    # CASO DE USUARIO 4
    # Aplico el related para vincular los generos del autor con el del libro
    # No necesito establecer el parametro comodel_name
    # Este campo no será editable
    genre_ids = fields.Many2many(related="author_id.genre_ids",
                                 string="Genres")

    # Agregamos el listado de lineas con el distribuidor
    dealer_line_ids = fields.One2many(
        comodel_name='books.dealer.line',
        inverse_name='book_id', string='Dealers')
    # Agregamos el listado de lineas con la editorial
    editorial_line_ids = fields.One2many(
        comodel_name='books.editorial.line',
        inverse_name='book_id', string='Editorial')
