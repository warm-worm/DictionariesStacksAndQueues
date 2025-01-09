# Use a stack. Read the next characters of the expression. Skip all but the brackets. If it 
# is an opening bracket, put it on the stack. If it is a closing bracket, get the item from 
# the stack and compare whether it is a matching opening bracket.

import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()
    matching = {')':'(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.put(char)
        elif char in ')}]':
            if stack.empty() or stack.get() != matching[char]:
                return False # brackets not matching
    return stack.empty() #True if brackets in expression are ok (stack empty) of False otherwise

if brackets_ok(expression1):
   print('The brackets of expression 1 are correct.')
else:
   print('The brackets of expression 1 are incorrect.')

if brackets_ok(expression2):
   print('The brackets of expression 2 are correct.')
else:
    print('The brackets of expression 2 are incorrect.')

if brackets_ok(expression3):
   print('The brackets of expression 3 are correct.')
else:
    print('The brackets of expression 3 are incorrect.')