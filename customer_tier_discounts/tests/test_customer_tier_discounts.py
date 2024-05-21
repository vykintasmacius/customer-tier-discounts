from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestCustomerTierDiscounts(TransactionCase):
    def setUp(self): 
        super(TestCustomerTierDiscounts, self).setUp()
        self.partner = self.env['res.partner'].create({'name': 'Customer1'})
        self.tier_bronze = self.env['res.partner.tier'].create({'name': 'Bronze', 'discount_percentage': 10})
        self.tier_silver = self.env['res.partner.tier'].create({'name': 'Silver', 'discount_percentage': 20})
        self.product = self.env['product.product'].create({'name': 'Example', 'list_price': 40})
        self.order = self.env['sale.order'].create({
            'partner_id': self.partner.id,
            'order_line': [(0, 0, {'product_id': self.product.id, 'product_uom_qty': 1})],
        })

    def test_assign_tier(self):
        self.partner.tier_id = self.tier_bronze
        self.assertEqual(self.partner.tier_id, self.tier_bronze, "Customer failed getting assigned Bronze tier")

    def test_update_tier(self):
        self.partner.tier_id = self.tier_bronze
        self.partner.tier_id = self.tier_silver
        self.assertEqual(self.partner.tier_id, self.tier_silver, "Customer failed getting updated to Silver")

    def test_apply_tier_discount(self):
        self.partner.tier_id = self.tier_bronze
        self.order.write({'partner_id': self.partner.id})
        self.assertEqual(self.order.order_line[0].discount, 10, "Bronze tier discount is being applied incorrectly")
        self.partner.tier_id = self.tier_silver
        self.order.write({'partner_id': self.partner.id})
        self.assertEqual(self.order.order_line[0].discount, 20, "Silver tier discount is being applied incorrectly")

    def test_no_tier(self):
        self.assertEqual(self.order.order_line[0].discount, 0, "Discount is being applied even though the customer has no tier")

    def test_invalid_discount(self):
        with self.assertRaises(ValidationError):
            self.env['res.partner.tier'].create({'name': 'Invalid', 'discount_percentage': 150})