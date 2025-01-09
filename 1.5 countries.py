countries = [
{"name":"Poland", "population":38000000},
{"name":"Iceland", "population":380000},
{"name":"Switzerland", "population":8690000},
{"name":"Netherlands", "population":17700000},
{"name":"Japan", "population":125800000}
]
print('COUNTRY POPULATION')
for country in countries:
    print(f'{country["name"]}: {country["population"]}')
