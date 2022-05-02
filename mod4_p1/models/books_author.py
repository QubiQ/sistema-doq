from odoo import fields, models


class BookAuthor(models.Model):
    _name = 'books.author'
    _description = 'autores'

    name = fields.Char(string="Name")
    books_ids = fields.One2many(
        comodel_name='books.book', inverse_name='author_id', string='Books')
