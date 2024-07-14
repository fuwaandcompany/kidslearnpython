# Task 8: Find the Maximum and Minimum in a List
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]
maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)
