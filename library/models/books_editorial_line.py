from odoo import api, fields, models


class BooksEditorialLine(models.Model):
    _name = 'books.editorial.line'
    _description = 'New Description'

    editorial_id = fields.Many2one(comodel_name='res.partner',
                                   string="Editorial")
    page_number = fields.Integer(string='Number of Pages')
    book_id = fields.Many2one(comodel_name='books.book')
