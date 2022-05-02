from odoo import fields, models


class ModuleAuth(models.Model):
    _name = 'books.author'
    _description = 'autores'

    name = fields.Char(required=True)
    books_ids = fields.One2many(
        comodel_name='books.book', inverse_name='author_id')
    genre_ids = fields.Many2many(comodel_name='books.genre', string="Genres")

    # Historia de usuario 2
    def unlink(self):
        for rec in self:
            rec.books_ids.unlink()
        return super().unlink()

    # Historia de usuario 5
    def write(self, values):
        # Primero escribo en el autor
        res = super().write(values)
        # los campos actualizados ahora estan en el self
        self.books_ids.write({'genre_ids': [(6, 0, self.genre_ids.ids)]})
        return res
