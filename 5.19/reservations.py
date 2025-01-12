##
# Program that prints the summary information as stated below. Break your program into 
# smaller parts defining functions.
# number of rooms
# number of paid reservations
# number of unpaid reservations
# total value of paid reservations
# total value of unpaid reservations
##

import json

def load_reservations(filename): #to load data from the file
    with open(filename, 'r') as file:
        return json.load(file)['reservations']
    
def number_of_rooms(reservations):
    return len(reservations)

def number_of_paid_reservations(reservations):
    return sum(1 for reservation in reservations if reservation['paid'])

def number_of_unpaid_reservations(reservations):
    return sum(1 for reservation in reservations if not reservation['paid'])

def total_value_of_paid_reservations(reservations):
    total = 0
    for reservation in reservations:
        if reservation['paid']:
            total += reservation['nights'] * reservation['price_per_night']
    return total

def total_value_of_unpaid_reservations(reservations):
    total = 0
    for reservation in reservations:
        if not reservation['paid']:
            total += reservation['nights'] * reservation['price_per_night']
    return total

def summary_information(filename):
    reservations = load_reservations(filename)

    total_rooms = number_of_rooms(reservations)
    number_paid = number_of_paid_reservations(reservations)
    number_unpaid = number_of_unpaid_reservations(reservations)
    paid_value = total_value_of_paid_reservations(reservations)
    unpaid_value = total_value_of_unpaid_reservations(reservations)

    print(f'Total number of rooms: {total_rooms}.')
    print(f'Number of paid reservations: {number_paid}.')
    print(f'Number of unpaid reservations: {number_unpaid}.')
    print(f'Total value of paid reservations: {paid_value}.')
    print(f'Total value of unpaid reservations: {unpaid_value}.')

summary_information('reservations.json')