# Creating a dictionary
my_dict = {"apple": 10, "banana": 20, "orange": 15}
print("Original Dictionary:", my_dict)

# Accessing elements in a dictionary
print("Value of 'apple':", my_dict["apple"])
print("Value of 'banana':", my_dict.get("banana"))

# Adding or updating elements in a dictionary
my_dict["mango"] = 25
print("After adding 'mango':", my_dict)

my_dict.update({"grapes": 30, "apple": 12,"grapes": 45})
print("After updating 'apple' and adding 'grapes':", my_dict)

# Removing elements from a dictionary
del my_dict["orange"]
print("After deleting 'orange':", my_dict)

popped_value = my_dict.pop("banana")
print("Popped value:", popped_value)
print("After popping 'banana':", my_dict)

# Clearing the dictionary
my_dict.clear()
print("After clearing the dictionary:", my_dict)

# Creating a new dictionary
my_dict = {"apple": 10, "banana": 20, "orange": 15}

# Copying the dictionary
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)

# Getting keys and values
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())

# Getting items (key-value pairs)
print("Items:", my_dict.items())

# Iterating through a dictionary
for key in my_dict:
    print(key, ":", my_dict[key])

# Length of the dictionary
print("Length of the dictionary:", len(my_dict))

# Check if key exists in dictionary
print("Is 'banana' in dictionary?", "banana" not in my_dict)

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print("Squared Dictionary:", squared_dict)

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)

# Sorting dictionaries
sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}
print("Sorted Dictionary:", sorted_dict)
