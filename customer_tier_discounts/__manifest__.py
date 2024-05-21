{
    'name': 'Customer Tier Discounts',
    'category': 'Sales',
    'summary': 'Manage product discounts based on customer tiers',
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/menu_views.xml',
    ],
    'depends': [
        'sale',
        'sale_management'
    ],
    'installable': True,
    'auto_install': False,
}
