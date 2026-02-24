# Temperature Converter

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


while True:

    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("Exiting program.")
        break

    if choice >= 1 and choice <= 6:

        temp = float(input("Enter the temperature: "))

        if choice == 1:
            result = celsius_to_fahrenheit(temp)
        elif choice == 2:
            result = fahrenheit_to_celsius(temp)
        elif choice == 3:
            result = celsius_to_kelvin(temp)
        elif choice == 4:
            result = kelvin_to_celsius(temp)
        elif choice == 5:
            result = fahrenheit_to_kelvin(temp)
        elif choice == 6:
            result = kelvin_to_fahrenheit(temp)

        print("Converted temperature:", round(result, 2))

    else:
        print("Invalid choice. Please select between 1 and 7.")