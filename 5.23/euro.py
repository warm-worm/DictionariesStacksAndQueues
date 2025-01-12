import json

with open('euro.json', 'r') as file:
    data = json.load(file)

print('Date            Buying Rate     Selling Rate')
print('============================================')

for rate in data['rates']:
    date = rate['effectiveDate']
    buying_rate = rate['bid']
    selling_rate = rate['ask']
    print(f'{date}      {buying_rate}          {selling_rate}')