
def find_greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
print("Enter three numbers:")
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
num3 = float(input("Number 3: "))
greatest = find_greatest(num1, num2, num3)
print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")
