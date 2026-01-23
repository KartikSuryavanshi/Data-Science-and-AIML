"""While Loop:

The while loop repeats a block of code as long as a specified condition is true.
while condition:
    # code block

For Loop:

The for loop iterates over a sequence or any iterable object.
for element in iterable:
    # code block

Range Loop:

The range() function generates a sequence of numbers which is commonly used with for loop to iterate a specific number of times.
for i in range(start, stop, step):
    # code block

Nested Loops:

You can use loops inside other loops, known as nested loops, to perform more complex iterations.   
for i in range(5):
    for j in range(3):
        # code block
    
Loop Control Statements:

Break: Terminates the loop prematurely when a condition is met.
for element in iterable:
    if condition:
        break
Continue: Skips the current iteration and proceeds to the next one.

for element in iterable:
    if condition:
        continue
Pass: Acts as a placeholder, does nothing when executed. It is used when a statement is syntactically required but you don't want any code execution.
for element in iterable:
    pass"""

# While Loop:
print("While Loop:")
num = 1
while num <= 5:
    print(num)
    num += 1

# For Loop:
print("\nFor Loop:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop Control Statements:
print("\nLoop Control Statements:")
num = 0
while num < 5:
    num += 1
    if num == 3:
        break  # Breaks out of the loop when num equals 3
    print(num)

for letter in 'python':
    if letter == 'h':
        continue  # Skips the iteration when letter is 'h'
    print(letter)

for i in range(3):
    pass  # Acts as a placeholder, does nothing

# Nested Loops:
print("\nNested Loops:")
for i in range(2):
    for j in range(3):
        print(i, j)
