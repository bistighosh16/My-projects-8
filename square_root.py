
number = float(input("Enter a number: "))
if number >= 0:
    square_root = number ** 0.5
    print(f"The square root of {number} is: {square_root:.2f}")
else:
    print("Square root of a negative number is not real.")
