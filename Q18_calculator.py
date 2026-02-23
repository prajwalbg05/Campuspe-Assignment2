def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return round(x / y, 2)

def modulus(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x % y

def power(x, y):
    return x ** y

if __name__ == "__main__":
    while True:
        print("\nCalculator Menu:")
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1','2','3','4','5','6']:

            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(a, b))

            elif choice == '2':
                print("Result:", subtract(a, b))

            elif choice == '3':
                print("Result:", multiply(a, b))

            elif choice == '4':
                print("Result:", divide(a, b))

            elif choice == '5':
                print("Result:", modulus(a, b))

            elif choice == '6':
                print("Result:", power(a, b))

        else:
            print("Invalid input. Please enter a number between 1 and 7.")