##
# program that calculates and displays the average price for a room in hotels in Krakow and 
# Sopot and indicates in which cities hotels are cheaper
##

def hotel_list(hotels):
    return ", ".join([hotel['name'] for hotel in hotels])

def avg_price(hotels):
    total_price = sum(hotel['price'] for hotel in hotels)
    return round(total_price / len(hotels))

hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

krakow_hotels = hotel_list(hotels_in_Krakow)
sopot_hotels = hotel_list(hotels_in_Sopot)

krakow_avg_price = avg_price(hotels_in_Krakow)
sopot_avg_price = avg_price(hotels_in_Sopot)

print(f'Hotels in Krakow: {krakow_hotels}')
print(f'Average hotel price in Krakow: {krakow_avg_price}')
print(f'Hotels in Sopot: {sopot_hotels}')
print(f'Average hotel price in Sopot: {sopot_avg_price}')

if krakow_avg_price < sopot_avg_price:
    print(f'Cheaper hotels in: Kraków')
elif sopot_avg_price < krakow_avg_price:
    print(f'Cheaper hotels in: Sopot')
else:
    print('The pricing of the hotels in both cities is the same.')
