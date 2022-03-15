from odoo import api, fields, models


class BooksEditorialLine(models.Model):
    _name = 'books.editorial.line'
    _description = 'New Description'
    # CASO DE USUARIO 2
    # Editorial relacionado con el modelo contactos
    editorial_id = fields.Many2one(comodel_name='res.partner',
                                   string="Editorial")
    page_number = fields.Integer(string='Number of Pages')
    # Relacion necesaria para el One2many
    book_id = fields.Many2one(comodel_name='books.book')
