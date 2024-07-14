# Task 7: Calculate the Factorial of a Number
number = int(input("Enter a number to find its factorial: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial of", number, "is", factorial)
