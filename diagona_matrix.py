# Input the number of rows and columns for a square matrix
try:
    n = int(input("Enter the number of rows and columns: "))
    matrix = []
    print("Enter the matrix elements row by row :")
    for _ in range(n):
        row = input().split()
        matrix.append([int(x) for x in row])
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]
    print("Sum of diagonal elements:", diagonal_sum)
except ValueError:
    print("Invalid input. Please enter valid integers.")