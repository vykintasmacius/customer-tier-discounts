## Introduction

This is a brief report explaining the design decisions and any assumptions made.

## Design decisions

The given task did not allow for much flexibility - most of the important design decisions, such as overriding the `create` and `write` methods of the `sale.order` model were already outlined in the task. All that was left was to implement them based on best practices and examples from the Odoo documentation.

In terms of more vague stuff, such as the validity check if the discount percentage is between 0 and 100, I used `@api.constrains` decorator as it seemed to be the common practice for situations like this and I couldn't find better alternatives. 

I also ended up creating an extra menu item that allows to manage all of the customer tiers directly from the Sales configuration menu. While you can add or delete the tiers inside the customer form view, it's not necessarily the most convenient.

I made the discount field read-only so it cannot be modified by someone and is purely based on customer tiers.

## Assumptions

### Discount restrictions

It was assumed that the discount gets applied to all and any of the products that are inside the order lines.

### One tier per customer

It was assumed that each customer can be assigned to only one tier at a time.

### Access control

The instructions for access control rules were quite vague, thus I assumed that sale managers being the only ones that can read, create, edit and delete customer tiers is sufficient enough for the validation criteria. In real business environments, these rules should be modified based on their needs.

