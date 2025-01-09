##
# Program that converts any natural number to a binary number. To convert a number, divide 
# the number by 2, each time taking the remainder of the division and putting the remainder 
# on the stack. Repeat the division until the number you are dividing is zero. Then pop and 
# display all values from the stack
##
import queue

def natural_to_bin(n):
    if n <= 0:
        return "not natural"
    stack = queue.LifoQueue()
    while n > 0:
        remainder = n % 2
        stack.put(remainder)
        n = n // 2 # int division by 2
    bin_number = ''
    while not stack.empty():
        bin_number += str(stack.get()) #to append each number 
    return bin_number

number = int(input('Enter a natural number: '))
result = natural_to_bin(number)

if result != "not natural":
    print(f'The natural number {number} converted to binary is: {result}')
else:
    print('Enter a different number.')


    
