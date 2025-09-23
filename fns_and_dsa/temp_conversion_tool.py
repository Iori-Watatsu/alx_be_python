FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius():
    temp = int(input("Enter the temperature to convert: "))
    specify = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).upper()

    global FAHRENHEIT_TO_CELSIUS_FACTOR, CELSIUS_TO_FAHRENHEIT_FACTOR

    if specify == "F":
        conversion = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temp}°F is, {conversion}°C")
convert_to_celsius()

def convert_to_fahrenheit():
    temp = int(input("Enter the temperature to convert: "))
    specify = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).upper()

    global FAHRENHEIT_TO_CELSIUS_FACTOR, CELSIUS_TO_FAHRENHEIT_FACTOR

    if specify == "C":
        conversion = (temp * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32
    print(f"{temp}°C is, {conversion}°F")
convert_to_fahrenheit()