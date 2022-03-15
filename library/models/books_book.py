from odoo import fields, models


class BooksBook(models.Model):
    _name = 'books.book'
    _description = 'Books'
    # A pesar de el string ser opcional vamos a agregarlo
    # para tener consciencia de que existe
    # Nombre del libro - char
    name = fields.Char(string="Name")
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
    date = fields.Datetime(string='Purchase Date')
