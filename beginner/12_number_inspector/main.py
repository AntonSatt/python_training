def is_even(n):
    return n % 2 == 0


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n


def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


print("=== Number Inspector ===")

while True:
    raw = input("\nEnter a number (or 'q' to quit): ").strip()
    if raw.lower() == "q":
        print("Goodbye!")
        break

    try:
        n = int(raw)
        if n < 1:
            print("Please enter a positive integer.")
            continue
    except ValueError:
        print("Please enter a whole number.")
        continue

    factors = get_factors(n)
    print(f"\nInspecting {n}...")
    print(f"  Even/Odd   : {'Even' if is_even(n) else 'Odd'}")
    print(f"  Prime      : {'Yes' if is_prime(n) else 'No'}")
    print(f"  Perfect    : {'Yes' if is_perfect(n) else 'No'}")
    print(f"  Armstrong  : {'Yes' if is_armstrong(n) else 'No'}")
    print(f"  Palindrome : {'Yes' if is_palindrome(n) else 'No'}")
    print(f"  Factors    : {', '.join(str(f) for f in factors)}")
