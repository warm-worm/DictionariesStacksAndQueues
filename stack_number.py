import queue

numbers = queue.LifoQueue()

numbers.put(2)
numbers.put(3)
numbers.put(7)
numbers.put(4)
numbers.put(1)
numbers.put(9)
numbers.put(8)

last_two_sum = numbers.get() + numbers.get()

print(f'The sum of the last two numbers is {last_two_sum}')

remaining = 0
while not numbers.empty():
    remaining += numbers.get()

print(f'The sum of the remaining stack elements is {remaining}')