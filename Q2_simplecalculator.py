# Question 2: Simple Calculator

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults:")
# Addition
print(num1, "+", num2, "=", num1 + num2)
# Subtraction
print(num1, "-", num2, "=", num1 - num2)

# Multiplication
print(num1, "*", num2, "=", num1 * num2)

# Division
if num2 != 0:
    print(num1, "/", num2, "=", round(num1 / num2, 2))
else:
    print("cannot divide by zero")

# Modulus
if num2 != 0:
    print(num1, "%", num2, "=", num1 % num2)
else:
    print("cannot divide by zero")

# Exponentiation
print(num1, "^", num2, "=", num1 ** num2)