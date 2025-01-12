import json

# read product data from keyboard
name = input('Enter the name of the product: ')
price = round(float(input('Enter the price of the product: ')), 2)
paid = input('Have you paid for the product? (yes/no) ').strip().lower()

paid = paid == 'yes' #converts yes to True and no to False

product = {
   "name": name,
   "price": price,
   "paid": paid
}

# save product data to json file
file_name = "product.json"

# Open the file in write mode and use json.dump() to write the data to the file
with open(file_name, 'w') as file:
   json.dump(product, file, indent=4)

print("Data has been written to", file_name)