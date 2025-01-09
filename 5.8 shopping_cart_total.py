##
# Program to calculate the total cost of a shopping cart using a price list
#

# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
rounded_total_cost = round(sum(prices[item] * quantity for item, quantity in cart.items()), 20)

print(f'Total cost: {rounded_total_cost}')
