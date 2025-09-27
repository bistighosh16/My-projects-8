import cmath
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
if a == 0:
    print("The equation is not quadratic (a cannot be zero).")
else:
    discriminant = (b ** 2) - (4 * a * c)
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    print(f"The roots of the quadratic equation are:")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
