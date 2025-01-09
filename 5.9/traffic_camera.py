##
# Program that calculates and prints how many registered cars come from each province of Poland
##
province = {}

with open('province.csv', 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    for line in lines[1:]: # skipping the header
        letter, name = line.strip().split(',') #strip to get rid of spaces and stuff
        province[letter] = name

vehicle_count = {name: 0 for name in province.values()} #dictionary to count vehicles for each province

with open('vehicle.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        registration = line.strip()
        if registration: #no empty lines
            first_letter = registration[0].upper()
            if first_letter in province:
                province_name = province[first_letter] #getting province name
                vehicle_count[province_name] += 1 #increment count for the province

for province, count in vehicle_count.items():
    print(f'{province}: {count} vehicles.')