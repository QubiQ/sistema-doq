from odoo import fields, models, api


class BooksGenre(models.Model):
    _name = 'books.book'
    _description = 'Books'

    name = fields.Char(required=True)
    price = fields.Float(string="Price")
    edition = fields.Integer(string="Edition")
    book_type = fields.Selection(
        string="Type",
        selection=[('fisico', 'Fisico'), ('digital', 'Digital')])
    website = fields.Char(string="Website")
    available = fields.Boolean(string="Available")
    date = fields.Date(string='Purchase Date')
    genre_ids = fields.Many2many(comodel_name='books.genre', string="Genres")
    author_id = fields.Many2one(string="Author", comodel_name='books.author')
    dealer_line_ids = fields.One2many(
        comodel_name='books.dealer.line',
        inverse_name='book_id', string='Dealers')

    editorial_line_ids = fields.One2many(
        comodel_name='books.editorial.line',
        inverse_name='book_id', string='Editorial')

    # 1º Historia de Usuario
    @api.onchange('author_id')
    def onchange_author_id(self):
        if self.author_id:
            self.genre_ids = self.author_id.genre_ids

    # 2º Historia de Usuario
    total_units = fields.Float(compute="_compute_total_units")
    # 3º Historia de Usuario
    total_sales = fields.Float(compute="_compute_total_units")
    # 4º Historia de Usuario
    full_name = fields.Char(compute="_compute_full_name",
                             store=True, readonly=False)

    @api.depends('price', 'dealer_line_ids')
    def _compute_total_units(self):
        # Hacemos esto para recorrer el recordset
        # Si no lo hacemos dara error singleton al cargar un listado de libros
        for rec in self:
            rec.total_units = 0
            for dealer in rec.dealer_line_ids:
                # 2º Historia de usuario
                rec.total_units += dealer.sale_unit
            # 3º Historia de usuario
            rec.total_sales = rec.total_units * rec.price

    # 4º Historia de Usuario
    @api.depends('name', 'author_id')
    def _compute_full_name(self):
        for rec in self:
            if rec.name:
                rec.full_name = rec.name
            if rec.author_id:
                rec.full_name += ' - ' + rec.author_id.name
