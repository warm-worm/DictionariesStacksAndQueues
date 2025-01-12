##
# Program that supports customer service in an office. Each new customer receives a ticket 
# with an automatically assigned consecutive number and is added to the end of the queue. 
# The next customer to be served is taken from the beginning of the queue.
##

def customer_service():
    queue = []
    ticket_number = 1 #to start assigning tickets from 1
    while True:
        queue.append(ticket_number)
        print(f'Customer with ticket number {ticket_number} has been added to the queue.')
        ticket_number += 1 #incrementing for the next customer

        if queue: #checking if there are customers to serve
            served_customer = queue.pop(0) #to serve the first customer in the queue
            print(f'Customer with ticket number {served_customer} is being served right now.')
        
        quit_program = input("Type 'Q' to quit or press Enter to continue.")
        if quit_program == 'Q':
            print('Exiting the customer service program.')
            break

customer_service() #to run the program

