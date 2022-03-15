from odoo import fields, models


class BooksBook(models.Model):
    _inherit = 'books.book'

    page_number = fields.Integer(string="Number of Pages")
    date = fields.Date(string="Date")
    name = fields.Char(required=True)