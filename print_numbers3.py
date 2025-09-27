
n = int(input("Enter the value of n: "))
series_sum = 0
product = 1  
for i in range(1, n + 1):
    product *= i  
    series_sum += product  
print(f"The sum of the series is: {series_sum}")
