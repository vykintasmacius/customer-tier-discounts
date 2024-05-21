from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ResPartnerTier(models.Model):
    _name = 'res.partner.tier'
    _description = 'Customer Tier'

    name = fields.Char(string='Tier', required=True)
    discount_percentage = fields.Float(string='Discount Percentage', required=True)

    @api.constrains('discount_percentage')
    def _check_discount(self):
        for tier in self:
             if tier.discount_percentage < 0 or tier.discount_percentage > 100:
                 raise ValidationError("Discount percentage must be between 0 and 100")