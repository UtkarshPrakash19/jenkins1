def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a number: "))

# Calculating the factorial
result = factorial(num)

print(f"The factorial of {num} is =  {result}")
