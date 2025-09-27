def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("Enter the matrix elements row by row:")
for i in range(rows):
    matrix.append(list(map(int, input().split())))
print("\nThe Matrix is:")
print_matrix(matrix)
