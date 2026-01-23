# Function to take matrix input from user
def input_matrix(rows, cols):
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

# Function to display matrix
def display_matrix(matrix):
    for row in matrix:
        print(row)

# Function to perform matrix addition
def matrix_addition(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Function to perform matrix subtraction
def matrix_subtraction(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

# Function to perform matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)
    return result

# Function to calculate transpose of a matrix
def matrix_transpose(matrix):
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transpose

# Main program
rows = int(input("Enter the number of rows in the matrix: "))
cols = int(input("Enter the number of columns in the matrix: "))

print("\nEnter elements for first matrix:")
matrix1 = input_matrix(rows, cols)

print("\nEnter elements for second matrix:")
matrix2 = input_matrix(rows, cols)

print("\nMatrix 1:")
display_matrix(matrix1)

print("\nMatrix 2:")
display_matrix(matrix2)

# Addition
print("\nMatrix Addition:")
result_addition = matrix_addition(matrix1, matrix2)
display_matrix(result_addition)

# Subtraction
print("\nMatrix Subtraction:")
result_subtraction = matrix_subtraction(matrix1, matrix2)
display_matrix(result_subtraction)

# Multiplication
print("\nMatrix Multiplication:")
result_multiplication = matrix_multiplication(matrix1, matrix2)
display_matrix(result_multiplication)

# Transpose
print("\nTranspose of Matrix 1:")
transpose_matrix1 = matrix_transpose(matrix1)
display_matrix(transpose_matrix1)

print("\nTranspose of Matrix 2:")
transpose_matrix2 = matrix_transpose(matrix2)
display_matrix(transpose_matrix2)
