## Introduction

This is a brief report explaining the design decisions and any assumptions made.

## Design decisions

The given task did not allow for much flexibility - most of the important design decisions, such as overriding the `create` and `write` methods of the `sale.order` model were already outlined in the task. All that was left was to implement them based on best practices and examples from the Odoo documentation.

For more vague stuff, such as the validity check if the discount percentage is between 0 and 100, I used the `@api.constrains` decorator as it seemed to be the common practice for situations like this and I couldn't find better alternatives. 

I also ended up creating an extra menu item that allows to manage all of the customer tiers directly from the Sales configuration menu. While you can add or delete the tiers inside the customer form view, it's not necessarily the most convenient.

## Assumptions

### Discount calculations

Based on the instructions that `the discount is applied dynamically based on the customer’s tier at the time of order creation and when the order is updated`, I assumed that in the rare event that the user's order gets updated and his tier has changed since the initial order, the discount of his new current tier will be applied instead.

### Discount restrictions

It was assumed that the discount applies to all products inside the order lines.

### One tier per customer

It was assumed that each customer can be assigned to only one tier at a time.

### Access control

The instructions for access control rules were quite vague, so I assumed that sales managers being the only ones who can read, create, edit, and delete customer tiers is sufficient for the validation criteria. In real business environments, these rules should be modified based on customers' needs.

