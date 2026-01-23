# Creating an empty list
my_list = []
print("Empty list:", my_list)

# Adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
print("After adding elements:", my_list)

# Extending the list with another list
my_list.extend([40, 50])
print("After extending:", my_list)

# Inserting element at a specific index
my_list.insert(2, 25)
print("After inserting at index 2:", my_list)

# Removing element from the list
my_list.remove(25)
print("After removing 25:", my_list)

# Popping elements from the list
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After popping last element:", my_list)

popped_element = my_list.pop(1)
print("Popped element at index 1:", popped_element)
print("After popping element at index 1:", my_list)

# Clearing the list
my_list.clear()
print("After clearing the list:", my_list)

# Creating a new list
my_list = [10, 20, 30, 40, 50]

# Accessing elements using index
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Slicing from index 1 to 3:", my_list[1:3])

# Finding index of an element
print("Index of 30:", my_list.index(30))

# Counting occurrences of an element
print("Count of 20:", my_list.count(20))

# Reversing the list
my_list.reverse()
print("Reversed list:", my_list)

# Sorting the list
my_list.sort()
print("Sorted list:", my_list)

# Copying the list
copied_list = my_list.copy()
print("Copied list:", copied_list)

# Creating a list with repetition
repeated_list = [0] * 5
print("Repeated list:", repeated_list)

# Concatenating lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

# Nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested_list)
