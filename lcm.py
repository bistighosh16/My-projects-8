
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x
def compute_lcm(x, y):
    return abs(x * y) // compute_hcf(x, y)
lcm = compute_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm}.")
