from odoo import fields, models


class BookAuthor(models.Model):
    _name = 'books.author'
    _description = 'autores'

    name = fields.Char(required=True, string="Name")
    books_ids = fields.One2many(
        comodel_name='books.book', inverse_name='author_id', string='Books')

    genre_ids = fields.Many2many(comodel_name='books.genre', string="Genres")
