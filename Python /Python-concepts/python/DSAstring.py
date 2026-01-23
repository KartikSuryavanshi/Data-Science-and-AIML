# Creating a string
my_string = """Hello's, World!"""
print("Original String:", my_string)

# Accessing characters in a string
print("First character:", my_string[0])
print("Last character:", my_string[-1])
print("Slicing from index 1 to 4:", my_string[1:5])

# Length of a string
print("Length of the string:", len(my_string))

# Converting to upper case and lower case
print("Upper case:", my_string.upper())
print("Lower case:", my_string.lower())

# Capitalizing the first character
print("Capitalized string:", my_string.capitalize())

# Checking if the string starts or ends with a specific substring
print("Starts with 'Hello':", my_string.startswith("Hello"))
print("Ends with 'World!':", my_string.endswith("World!"))

# Finding the index of a substring
print("Index of 'World':", my_string.find("World"))

# Counting occurrences of a substring
print("Count of 'l':", my_string.count("l"))

# Replacing substrings
print("After replacing 'Hello' with 'Hi':", my_string.replace("Hello", "Hi"))

# Splitting a string into a list of substrings
print("Splitting the string:", my_string.split(","))

# Joining a list of substrings into a string
my_list = ["apple", "banana", "orange"]
print("Joining the list:", "! ".join(my_list))

# Stripping leading and trailing whitespace
my_string_with_spaces = "  Hello,World!  "
print("Stripped string:", my_string_with_spaces.strip())

# Checking if the string contains only alphabetic characters or digits
print("Is alphabetic:", my_string.isalpha())
print("Is digit:", my_string.isdigit())

# Checking if the string is titlecased
print("Is titlecased:", my_string.istitle())

# Checking if the string is in a specific format
print("Is formatted as an email:", my_string.endswith("@example.com"))

# Formatting strings
name = "Alice"
age = 30
print("Formatted string:", "Name: {}, Age: {}".format(name, age))
print("Formatted string (f-string):", f"Name: {name}, Age: {age}")
