
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))
divisor = int(input("Enter the number to check divisibility: "))
print(f"Numbers divisible by {divisor} between {start} and {end} are:")
for num in range(start, end + 1):
    if num % divisor == 0:
        print(num, end=" ")
