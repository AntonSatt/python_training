import time


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number.")


print("=== Countdown Timer ===")

while True:
    minutes = get_positive_int("Set timer — Minutes: ")
    seconds = get_positive_int("             Seconds: ")

    total = minutes * 60 + seconds
    if total == 0:
        print("Timer must be longer than 0 seconds.")
        continue

    remaining = total
    while remaining >= 0:
        mins, secs = divmod(remaining, 60)
        print(f"\r  \u23f1  {mins:02d}:{secs:02d} remaining...", end="", flush=True)
        if remaining == 0:
            break
        time.sleep(1)
        remaining -= 1

    print("\n\n\U0001f514 Time's up!\n")

    again = input("Set another timer? (y/n): ").lower().strip()
    if again != "y":
        print("Goodbye!")
        break
