
number = int(input("Enter a number to display its multiplication table: "))
table_range = int(input("Enter the range for the multiplication table (e.g., 10 for 1 to 10): "))
print(f"\nMultiplication table for {number} is:")
for i in range(1, table_range + 1):
    result = number * i
    print(f"{number} x {i} = {result}")
