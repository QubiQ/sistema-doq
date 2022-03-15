from odoo import fields, models


class BooksGenre(models.Model):
    # Nombre con el que nos referiremos al módulo
    _name = 'books.genre'
    _description = 'Books Genre'
    # Campo de nombre de tipo char.
    name = fields.Char()
