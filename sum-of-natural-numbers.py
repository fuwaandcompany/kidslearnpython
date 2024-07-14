# Task 10: Sum of Natural Numbers
N = int(input("Enter a number to find the sum of the first N natural numbers: "))
sum_of_numbers = 0

for i in range(1, N + 1):
    sum_of_numbers += i

print("Sum of the first", N, "natural numbers is", sum_of_numbers)
