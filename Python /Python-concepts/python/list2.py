# List Creation:
empty_list = []
list_with_values = [1, 2, 3, 4, 5]

# Accessing Elements:
my_list = [10, 20, 30, 40, 50]
print("Accessing Elements:")
print(my_list[0])         # Output: 10
print(my_list[-1])        # Output: 50 (Accessing last element)

# Slicing:
print("\nSlicing:")
print(my_list[1:4])       # Output: [20, 30, 40]

# Common Operations:
print("\nCommon Operations:")
concatenated_list = [1, 2, 3] + [4, 5, 6]  # Output: [1, 2, 3, 4, 5, 6]
print("Concatenation:", concatenated_list)
repeated_list = [0] * 3                  # Output: [0, 0, 0]
print("Repetition:", repeated_list)

# List Methods:
my_list = [10, 20, 30, 40, 50]
my_list.append(60)                       # Append
my_list.insert(2, 25)                    # Insert
my_list.remove(40)                       # Remove
popped_element = my_list.pop()           # Pop
index = my_list.index(30)                # Index
count = my_list.count               # Count
my_list.sort()                           # Sort
my_list.reverse()                        # Reverse
my_list.clear()                          # Clear
copy_of_list = my_list.copy()            # Copy

print("\nList Methods:")
print("Append 60:", my_list)
print("Insert 25 at index 2:", my_list)
print("Remove 40:", my_list)
print("Popped element:", popped_element)
print("Index of 30:", index)
print("Count of 20:", count)
print("Sorted list:", my_list)
print("Reversed list:", my_list)
print("Cleared list:", my_list)
print("Copy of list:", copy_of_list)

# List Comprehension:
squares = [x**2 for x in range(5)]       # Output: [0, 1, 4, 9, 16]
print("\nList Comprehension:")
print("Squares:", squares)
