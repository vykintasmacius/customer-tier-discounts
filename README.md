## Overview

This custom Odoo module extends the functionality of the Sales module by adding a feature to manage product discounts based on customer tiers.

## Setup

1. Clone this repository or download and uncompress the ZIP to your local machine.

2. Move or copy the `customer_tier_discounts` folder inside your Odoo installation's `addons` folder. The end of the path should read `odoo/addons/customer_tier_discounts.`

3. Run or restart your Odoo server, go to `Apps`, and click `Update Apps List`. Use the search bar to find `Customer Tier Discounts` and click `Install`.

If the module does not appear, remove the default `Apps` filter and search again.

## Dependencies

The module has two dependencies: `sale` and `sale_management.` They should be installed automatically once the module is activated. However, if you can't see its UI, ensure these dependencies are installed/activated, as that could be the reason it doesn't work.

## Usage

1. **Creating a tier**:
- First, go to `Sales -> Configuration -> Customer Tiers.` Then click `New` and populate the name and discount fields accordingly.
- To delete a tier, select it and click `Actions -> Delete.`
- Tiers can also be created inside each customer's form view (see below).

2. **Assigning a tier**:
- Navigate to the customer's form view for which you want a tier assigned.
- Click on `Sale & Purchases` tab and scroll until you see a `Customer Tier` section. 
- Use it to assign, unassign or create a new tier.

3. **Creating an order**:
- You can create an order by going to `Sales -> Orders -> Orders.`
- Once created or updated, the appropriate discount is applied based on the customer's tier.

## Unit tests

The `tests` folder contains unit tests that cover:
- Creation and assignment of different tiers to customers
- Different discount applications based on tiers
- Edge cases (no tier, discount percent over 100, etc.)

Tests can be run using the following command once you are inside your Odoo directory:

```bash
python3 odoo-bin -i customer_tier_discounts --log-level=test -d mydb --test-enable --stop-after-init
```

Where `mydb` is the name of your databse.

If everything is set up correctly, the module should be able to pass all tests. Observe the `odoo.log` file for any messages.

## License

This module is released under the MIT License. See [LICENSE](LICENSE) for further details.