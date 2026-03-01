def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


ops = {
    "1": (add, "+"),
    "2": (subtract, "-"),
    "3": (multiply, "*"),
    "4": (divide, "/"),
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


print("=== Calculator ===")

while True:
    print("\n[1] Add  [2] Subtract  [3] Multiply  [4] Divide  [5] Quit")
    choice = input("\nChoose operation: ").strip()

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ops:
        print("Invalid choice. Please pick 1–5.")
        continue

    func, symbol = ops[choice]
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    result = func(a, b)
    if result is None:
        print("Error: can't divide by zero!")
    else:
        print(f"{a} {symbol} {b} = {result}")
