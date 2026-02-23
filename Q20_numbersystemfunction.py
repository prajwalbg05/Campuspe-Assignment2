# Create the following mathematical functions: 
# 1. factorial(n) - return n! 
# 2. is_prime(n) - return True if prime 
# 3. fibonacci(n) - return nth Fibonacci number 
# 4. sum_of_digits(n) - return sum of digits 
# 5. reverse_number(n) - return number reversed 
# 6. is_armstrong(n) - check if Armstrong number (e.g., 153 = 1³ + 5³ + 3³) 
# 7. gcd(a, b) - greatest common divisor 
# 8. lcm(a, b) - least common multiple 
# 9. is_perfect_number(n) - sum of divisors equals n (e.g., 6 = 1+2+3) 
# 10. math_menu() - menu to test all functions 
# Each function should be callable individually from the menu with appropriate user input.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <  0:
        return "Fibonacci is not defined for negative numbers."
    elif n == 0:
        return 0
    elif n == 1:
        return 1  
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
def reverse_number(n):
    return int(str(abs(n))[::-1])
def is_armstrong(n):
    num_str = str(abs(n))
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == abs(n)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
def is_perfect_number(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
def math_menu():    
    while True:
        print("\nMath Functions Menu:")
        print("1. Factorial")
        print("2. Check Prime")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Check Armstrong")
        print("7. GCD")
        print("8. LCM")
        print("9. Check Perfect Number")
        print("10. Exit")

        choice = input("Enter choice (1-10): ")

        if choice == '10':
            print("Exiting the math menu. Goodbye!")
            break

        if choice in ['1','2','3','4','5','6','7','8','9']:
            if choice in ['1', '3']:
                n = int(input("Enter a number: "))
                if choice == '1':
                    print(f"Factorial of {n} is {factorial(n)}")
                else:
                    print(f"{n}th Fibonacci number is {fibonacci(n)}")

            elif choice in ['2', '6', '9']:
                n = int(input("Enter a number: "))
                if choice == '2':
                    print(f"{n} is {'a prime number' if is_prime(n) else 'not a prime number'}")
                elif choice == '6':
                    print(f"{n} is {'an Armstrong number' if is_armstrong(n) else 'not an Armstrong number'}")
                else:
                    print(f"{n} is {'a perfect number' if is_perfect_number(n) else 'not a perfect number'}")

            elif choice in ['4', '5']:
                n = int(input("Enter a number: "))
                if choice == '4':
                    print(f"Sum of digits of {n} is {sum_of_digits(n)}")
                else:
                    print(f"Reverse of {n} is {reverse_number(n)}")

            elif choice in ['7', '8']:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                if choice == '7':
                    print(f"GCD of {a} and {b} is {gcd(a, b)}")
                else:
                    print(f"LCM of {a} and {b} is {lcm(a, b)}")

        else:
            print("Invalid choice. Please try again.")
math_menu() 