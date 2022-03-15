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
    available = fields.Boolean(compute="_compute_available", store=True)
    date = fields.Date(string='Purchase Date')
    # Fecha de alquiler - Datetime
    last_renting_date = fields.Datetime(string='Last Renting')
    # Estado
    state = fields.Selection(
        selection=[('in_stock', 'In Stock'),
                   ('renting', 'Renting'),
                   ('lost', 'Lost')])
    author_id = fields.Many2one(comodel_name='books.author')
    genre_ids = fields.Many2many(comodel_name='books.genre',
                                 string="Genres")

    dealer_line_ids = fields.One2many(
        comodel_name='books.dealer.line',
        inverse_name='book_id', string='Dealers')
    editorial_line_ids = fields.One2many(
        comodel_name='books.editorial.line',
        inverse_name='book_id', string='Editorial')

    # Historia de usuario 4
    @api.depends('state')
    def _compute_available(self):
        for rec in self:
            rec.available = rec.state == "in_stock"
    # # Historia de usuario 1
    @api.model
    def create(self, values):
        print(values)
        if 'barcode' in values and values['barcode']:
            if self.search([('barcode', '=', values['barcode'])]):
                raise UserError("There is a book with the same ISBN %s" %
                                values['barcode'])
            if len(values['barcode']) != 13:
                raise UserError("The ISBN must to have 13 characters")
        return super().create(values)

    # Historia de usuario 3
    def write(self, values):
        if values.get('state') == 'renting':
            values['last_renting_date'] = fields.Datetime.now()
        return super().write(values)