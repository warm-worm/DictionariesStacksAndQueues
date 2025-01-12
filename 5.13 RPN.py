##
# Program that calculates RPN expressions. A user can enter from the keyboard any number, 
# an operator (+ - * / ) or the equal sign (=).
# If the entered value is a number, push the number on to the stack
# If the entered value is an operator, pop two items from the top of the stack, do the 
# calculation, and push the result of the operation on to the stack.
# If the entered value is an equal sign, pop the final result from the stack and display 
# the result of calculation.
##

def calculate_rpn():
    stack = []

    while True:
        user_input = input('Enter number, operator (+ - * /) or "=" to get the result: ')
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            stack.append(float(user_input)) #making it a float, could be int tho
        elif user_input in ['+', '-', '*', '/']:
            b = stack.pop() #popping two numbers
            a = stack.pop()
            if user_input == '+':
                stack.append(a + b)
            elif user_input == '-':
                stack.append(a - b)
            elif user_input == '*':
                stack.append(a * b)
            elif user_input == '/':
                stack.append(a / b)
        elif user_input == '=': #if '=' pop final result
            print(f'Result: {stack.pop()}')
            break
        else:
            print('Invalid input, try again.')

calculate_rpn() #to run the program
