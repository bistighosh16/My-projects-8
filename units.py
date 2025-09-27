
def calculate_bill(units):
    fixed_charge = 50  
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = (100 * 5) + (units - 100) * 7
    else:
        bill = (100 * 5) + (200 * 7) + (units - 300) * 10
    total_bill = bill + fixed_charge
    return total_bill
units = int(input("Enter the number of units consumed: "))
if units < 0:
    print("Invalid input. Units consumed cannot be negative.")
else:
    bill = calculate_bill(units)
    print(f"Number of Units Consumed: {units}")
    print(f"Electricity Bill: ₹{bill:.2f}")
