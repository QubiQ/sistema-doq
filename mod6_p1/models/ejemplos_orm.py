from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def button_create_project(self):
        # Boton para crear un projecto a raiz de un contacto
        vals = {
            'name': 'Project %s' % self.name,
            'parner_id': self.id,
        }
        self.env['project.project'].create(vals)

    @api.model
    def create(self, vals):
        '''params:
            vals -> Diccionario
            self -> Clase vacia
            return -> Devuelve el registro creado
        '''
        # Asigno el mismo nif de la empresa relacionada
        # Compruebo si tiene una empresa relacionada
        if "parent_id" in vals:
            # Busco la empresa relacionada y asigno su vat
            vals['vat'] = self.browse(vals["parent_id"]).vat
        # Add code here
        return super().create(vals)

    def write(self, vals):
        '''param:
            vals -> Dictionary
            self -> Just one record
            returns True

        '''
        # funcion para cambiar las etiquetas de los hijos despues de guardar
        res = super().write(vals)
        # Como hemos ejecutado el super podemos comprobar el campo desde el self
        # Escribo las etiquetas en los hijos
        self.child_ids.write(
                {'label_ids', [(6, 0, self.labels_ids.ids)]})
        return res

    def unlink(self):
        '''params:
            self -> record or recordset
        '''
        # Recoremos el recordset para borrar
        # los contactos hijos del contacto eliminado
        for record in self:
            if record.child_ids:
                record.child_ids.unlink()
        return super().unlink()
