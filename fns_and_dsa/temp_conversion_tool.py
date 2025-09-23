FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def celsius_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_temperature():
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if unit == "C":
        print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
    elif unit == "F":
        print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")
convert_temperature()
