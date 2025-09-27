
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))
print(f"Armstrong numbers between {start} and {end} are:")
for number in range(start, end + 1):
    num_digits = len(str(number))
    sum_of_powers = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    if number == sum_of_powers:
        print(number, end=" ")
