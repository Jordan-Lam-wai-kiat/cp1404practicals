temperature = float(input("Please enter a number for temperature: "))
choice_F_or_C = input("What would you like to convert it to? (C/F): ").upper()

def convert_to_celcius(F):
    """Converts Fahrenheit to Celcius"""
    celcius = ((F - 32) * 5) /9
    return celcius

def convert_to_fahrenheit(C):
    """Convert Celcius to Fahrenheit"""
    fahrenheit = (C * (9 / 5)) + 32
    return fahrenheit

if choice_F_or_C == "F":
    Fahrenheit = convert_to_fahrenheit(temperature)
    print("The temperature in Fahrenheit is: ", "%.1f" % Fahrenheit, "F")
elif choice_F_or_C == "C":
    celcius = convert_to_celcius(temperature)
    print("The temperature in Celcius is: ", "%.1f" % celcius, "C")
else:
    choice_F_or_C = input("Invalid choice, please enter F or C")