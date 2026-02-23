def celcius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celcius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celcius(kelvin):
    return kelvin - 273.15
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

options={
    1:celcius_to_fahrenheit,
    2:fahrenheit_to_celcius,
    3:celcius_to_kelvin,
    4:kelvin_to_celcius,
    5:fahrenheit_to_kelvin,
    6:kelvin_to_fahrenheit
}
print("Temperature Converter")
print("1. Celcius to Fahrenheit")
print("2. Fahrenheit to Celcius")
print("3. Celcius to Kelvin")
print("4. Kelvin to Celcius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")
choice=int(input("Enter your choice: "))        
if choice in options:
    temp=float(input("Enter the temperature: "))
    result=options[choice](temp)
    print("Converted temperature:", round(result, 2))
else:
    print("Invalid choice")