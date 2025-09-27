import random
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))
random_number = random.randint(lower_limit, upper_limit)
print(f"A random number between {lower_limit} and {upper_limit} is: {random_number}")
