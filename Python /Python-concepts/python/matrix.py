"""Matrix Basics:

A matrix is a two-dimensional data structure consisting of rows and columns.
It's commonly used for representing mathematical matrices, tables, or grids.
Creating Matrices:

Matrices can be created using nested lists or using libraries like NumPy.
Accessing Elements:

Elements in a matrix are accessed using row and column indices.
Operations on Matrices:

Matrices support various operations such as addition, subtraction, multiplication, and transpose."""

# Creating Matrices:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing Elements:
print("Accessing Elements:")
print(matrix[0][0])  # Output: 1 (First element)
print(matrix[1][2])  

# Operations on Matrices:
# Addition:
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result_addition = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result_addition[i][j] = matrix1[i][j] + matrix2[i][j]
print("Matrix Addition:")
for row in result_addition:
    print(row)

# Subtraction:
result_subtraction = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result_subtraction[i][j] = matrix1[i][j] - matrix2[i][j]
print("\nMatrix Subtraction:")
for row in result_subtraction:
    print(row)

# Multiplication:
result_multiplication = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result_multiplication[i][j] += matrix1[i][k] * matrix2[k][j]
print("\nMatrix Multiplication:")
for row in result_multiplication:
    print(row)

