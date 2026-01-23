# Defining tuples
tuple1 = (10, 20, 30)
tuple2 = (10, 20, "one", "two")

# Nested tuple
tuple3 = ("python", [10, 20, 30], [11, "abc"])
tuple4 = (10, 20, 30, 40)

# Note: Generating a tuple with a single element
tuple_single = (10,)  # Comma is necessary to differentiate from parentheses

# Tuple assignment
ojas = (1, "ojaswini", "jal")
(id_num, name, city) = ojas
print("ID:", id_num)

# Accessing elements in a tuple
tuple5 = (10, 20, 30, 40)
print("Element at index 1:", tuple5[1])
print("Elements from index 1 to 3:", tuple5[1:4])
print("Elements up to index 2:", tuple5[:2])

# Deleting tuples
t1 = (10, 20, 30, 40, 50)
# To remove a specific item, use slicing to exclude the item
t1 = t1[:2] + t1[3:]

# Converting tuple into list or vice versa
tuple6 = (1, 2, 3, 4, 5)
list1 = list(tuple6)
del list1[2]
tuple_from_list = tuple(list1)
print("Tuple from list:", tuple_from_list)

# Tuple operations
# 1. Concatenation and repetition
t1 = (10, 20, 30)
t2 = (40, 50, 60)
concatenated_tuple = t1 + t2
repeated_tuple = t1 * 2

# Membership function
# Check if item exists in tuple using the keyword 'in'
print("Is 30 in tuple t1:", 30 in t1)

# Iteration through a tuple
for item in tuple5:
    print(item)
