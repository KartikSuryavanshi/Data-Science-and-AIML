"""Tuples Basics:

Tuples are ordered collections of items.
Immutable: Once created, elements cannot be changed.
Heterogeneous: Tuples can contain items of different types.
Creating Tuples:

Tuples are created using parentheses () with comma-separated values.
Accessing Elements:

Elements are accessed using zero-based indexing.
Negative indexing starts from the end of the tuple.
Slicing:

Allows accessing a portion of the tuple using slicing notation [start:stop:step].
Common Operations:

Concatenation: + operator joins two tuples.
Repetition: * operator repeats a tuple.
Tuple Methods:

Tuples are immutable, so they have fewer methods compared to lists.
Methods include count() to count occurrences and index() to find the index of a value.
Tuple Packing and Unpacking:

Multiple values can be assigned to a tuple in a single statement (packing).
Individual values of a tuple can be assigned to variables (unpacking)."""
# Tuple Creation:
empty_tuple = ()
single_item_tuple = (42,)
multi_item_tuple = (1, 2, 3, 4, 5)

# Accessing Elements:
my_tuple = (10, 20, 30, 40, 50)
print("Accessing Elements:")
print(my_tuple[0])         # Output: 10
print(my_tuple[-1])        # Output: 50 (Accessing last element)

# Slicing:
print("\nSlicing:")
print(my_tuple[1:4])       # Output: (20, 30, 40)

# Common Operations:
print("\nCommon Operations:")
concatenated_tuple = (1, 2, 3) + (4, 5, 6)  # Output: (1, 2, 3, 4, 5, 6)
print("Concatenation:", concatenated_tuple)
repeated_tuple = (0,) * 3                  # Output: (0, 0, 0)
print("Repetition:", repeated_tuple)

# Tuple Methods:
my_tuple = (10, 20, 30, 40, 50)
count = my_tuple.count(20)                # Count
index = my_tuple.index(30)                # Index

print("\nTuple Methods:")
print("Count of 20:", count)
print("Index of 30:", index)



