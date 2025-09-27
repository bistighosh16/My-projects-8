
terms = int(input("Enter the number of terms: "))
powers_of_2 = list(map(lambda x: 2 ** x, range(terms)))
print(f"Powers of 2 for the first {terms} terms are:")
print(powers_of_2)
