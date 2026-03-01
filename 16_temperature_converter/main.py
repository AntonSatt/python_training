def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    return c + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


ABSOLUTE_ZERO_C = -273.15

conversions = {
    "1": ("°C", "°F", celsius_to_fahrenheit),
    "2": ("°F", "°C", fahrenheit_to_celsius),
    "3": ("°C", "K",  celsius_to_kelvin),
    "4": ("K",  "°C", kelvin_to_celsius),
    "5": ("°F", "K",  fahrenheit_to_kelvin),
    "6": ("K",  "°F", kelvin_to_fahrenheit),
}


def to_celsius(value, unit):
    if unit == "°C":
        return value
    if unit == "°F":
        return fahrenheit_to_celsius(value)
    return kelvin_to_celsius(value)


print("Temperature Converter")

while True:
    print("\n[1] °C→°F  [2] °F→°C  [3] °C→K  [4] K→°C  [5] °F→K  [6] K→°F  [7] Quit")
    choice = input("\nChoose: ").strip()

    if choice == "7":
        break

    if choice not in conversions:
        print("Invalid choice. Please pick 1–7.")
        continue

    from_unit, to_unit, func = conversions[choice]

    try:
        value = float(input(f"Enter temperature in {from_unit}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if to_celsius(value, from_unit) < ABSOLUTE_ZERO_C:
        print(f"Error: temperature cannot be below absolute zero (−273.15°C).")
        continue

    result = func(value)
    print(f"{value}{from_unit} = {round(result, 2)}{to_unit}")
