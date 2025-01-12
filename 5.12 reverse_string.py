##
# Define a function that takes a string as input and uses a stack to reverse it. Then, write 
# a program to reverse any text entered from the keyboard.
# Hint: Push each character of the string onto the stack, then pop characters to form the 
# reversed string.
##

def reverse_string(input_string):
    stack = []
    for char in input_string:
        stack.append(char)
    reversed_string = ''
    while stack:
        reversed_string += stack.pop() #pop from the stack gives in reverse
    return reversed_string

user_input = input('Enter a string to reverse: ')

print(f'Reversed string: {reverse_string(user_input)}.')
