#Extract two slices of a given list of numbers. Display and print the sum of first list slice which contain every other elements between
#index 5 to 15.Program should also display the average of second sliced list which contains every fourth element of list.The list
#contains 20 elements.
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
slice1 = numbers[5:16:2]  
sum_slice1 = sum(slice1)
slice2 = numbers[::4]  
average_slice2 = sum(slice2) / len(slice2) if slice2 else 0  
print("First sliced list:", slice1)
print("Sum of first sliced list:", sum_slice1)
print("Second sliced list:", slice2)
print("Average of second sliced list:", average_slice2)
