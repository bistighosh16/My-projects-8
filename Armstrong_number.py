
number = int(input("Enter a number: "))
num_digits = len(str(number))
sum_of_powers = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10
if number == sum_of_powers:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

