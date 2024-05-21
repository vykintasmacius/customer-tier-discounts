from odoo import api, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        order = super().create(vals)
        order.apply_discount()
        return order

    def write(self, vals):
        res = super().write(vals)
        self.apply_discount()
        return res

    def apply_discount(self):
        for order in self:
            if order.partner_id.tier_id:
                discount = order.partner_id.tier_id.discount_percentage
                for line in order.order_line:
                    line.discount = discount
            else:
                for line in order.order_line:
                    line.discount = 0