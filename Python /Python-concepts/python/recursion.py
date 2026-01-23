"""
Recursion in Python is a technique where a function calls itself in order to solve a problem.
Base Case: Define a base case that serves as the exit condition for the recursive function.

Recursive Case: Define the action to be performed in terms of smaller instances of the same problem.

Call the Function: Within the function, call itself with modified arguments to progress towards the base case.

Ensure Progress: Make sure each recursive call moves closer to the base case to avoid infinite recursion.

Clean Up: Handle any necessary cleanup after reaching the base case or after recursive calls."""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the fibonacci function
print("Fibonacci sequence:")
for i in range(10):
    print(fibonacci(i), end=" ")
