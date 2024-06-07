from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    purchase_order_ids = fields.One2many('purchase.order', 'sale_order_id', string='Purchase Orders')

    @api.model
    def create(self, vals):
        # Call super to invoke the original create method
        sale_order = super(SaleOrder, self).create(vals)

        # Prepare values for the purchase order
        purchase_order_vals = {
            'partner_id': sale_order.partner_id.id,
            'date_order': sale_order.date_order,
            'sale_order_id': sale_order.id,  # Link to the sale order
        }

        # Create the purchase order
        purchase_order = self.env['purchase.order'].create(purchase_order_vals)

        # Prepare values for the purchase order lines
        for line in sale_order.order_line:
            purchase_order_line_vals = {
                'product_id': line.product_id.id,
                'product_qty': line.product_uom_qty,
                'name': line.name,
                'price_unit': line.price_unit,
                'taxes_id': [(6, 0, line.tax_id.ids)],  # Many2many fields use this format
                'price_subtotal': line.price_subtotal,
                'order_id': purchase_order.id,
            }
            self.env['purchase.order.line'].create(purchase_order_line_vals)

        return sale_order

    def write(self, vals):
        # Call super to invoke the original write method
        res = super(SaleOrder, self).write(vals)

        for sale_order in self:
            for purchase_order in sale_order.purchase_order_ids:
                # Update the purchase order fields
                purchase_order.write({
                    'partner_id': sale_order.partner_id.id,
                    'date_order': sale_order.date_order,
                })

                # Get all the product IDs in the current sale order lines
                sale_order_product_ids = sale_order.order_line.mapped('product_id.id')
                # Remove purchase order lines that are no longer in the sale order
                purchase_order.order_line.filtered(lambda line: line.product_id.id not in sale_order_product_ids).unlink()

                for line in sale_order.order_line:
                    # Find the corresponding purchase order line
                    corresponding_line = self.env['purchase.order.line'].search([
                        ('order_id', '=', purchase_order.id),
                        ('product_id', '=', line.product_id.id)
                    ])
                    if corresponding_line:
                        # Update existing purchase order lines
                        corresponding_line.write({
                            'product_id': line.product_id.id,
                            'product_qty': line.product_uom_qty,
                            'name': line.name,
                            'price_unit': line.price_unit,
                            'taxes_id': [(6, 0, line.tax_id.ids)],
                            'price_subtotal': line.price_subtotal,
                        })
                    else:
                        # Create new purchase order lines for newly added sale order lines
                        purchase_order_line_vals = {
                            'product_id': line.product_id.id,
                            'product_qty': line.product_uom_qty,
                            'name': line.name,
                            'price_unit': line.price_unit,
                            'taxes_id': [(6, 0, line.tax_id.ids)],
                            'price_subtotal': line.price_subtotal,
                            'order_id': purchase_order.id,
                        }
                        self.env['purchase.order.line'].create(purchase_order_line_vals)

        return res

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
