
decimal_number = int(input("Enter a decimal number: "))
binary = bin(decimal_number)[2:]   
octal = oct(decimal_number)[2:]    
hexadecimal = hex(decimal_number)[2:].upper()  
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")

