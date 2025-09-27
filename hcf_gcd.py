
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x
hcf = compute_hcf(num1, num2)
print(f"The HCF or GCD of {num1} and {num2} is {hcf}.")
