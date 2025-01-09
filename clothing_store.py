# Due to a seasonal sale, the store is reducing the price of each item by 10%

price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print('Before the discount:')
for item, price in price_list.items():
    print(f'{item}: {price}')

total_value_before = round(sum(price_list.values()) , 2)
print(f'Total value of the products before the discount: {total_value_before}')

discounted_items = {item: round(price - (price * 10/100), 2) for item, price in price_list.items()}
print('After the discount:')
for item, price in discounted_items.items():
    print(f'{item}: {price}')

total_value_after = round(sum(discounted_items.values()), 2)
print(f'Total value of the products after the discount: {total_value_after}')