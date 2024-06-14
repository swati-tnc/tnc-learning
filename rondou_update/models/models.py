from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    quantity_custom = fields.Integer(string='Quantity', compute='_compute_quantity_custom')
    # unit_of_measurement_custom = fields.Selection([('gram', 'gram'), ('kg', 'kg'), ('stuk', 'stuk')], string='Unit of Measurement', default='gram')

    def _compute_quantity_custom(self):
        for product in self:
            if product.categ_id.name in ['All', 'Consumable']:
                product.quantity_custom = 50
            else:
                product.quantity_custom = 1
