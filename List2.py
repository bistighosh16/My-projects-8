numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:", even_numbers)