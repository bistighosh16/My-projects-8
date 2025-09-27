
def calculate_commission(sales):
    if sales < 500:
        commission_rate = 0.02  
    elif sales <= 1000:
        commission_rate = 0.05  
    elif sales <= 5000:
        commission_rate = 0.10 
    else:
        commission_rate = 0.15  
    
    commission = sales * commission_rate
    return commission, commission_rate * 100
sales = float(input("Enter the weekly sales of the salesman (in ₹): "))
commission, rate = calculate_commission(sales)
print(f"Weekly Sales: ₹{sales:.2f}")
print(f"Commission Rate: {rate}%")
print(f"Commission Earned: ₹{commission:.2f}")

