import random


def flip():
    return random.choice(["Heads", "Tails"])


while True:
    try:
        n = int(input("How many times should I flip the coin? "))
        if n <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a whole number.")

heads = 0
tails = 0

for i in range(1, n + 1):
    result = flip()
    print(f"Flip {i}: {result}")
    if result == "Heads":
        heads += 1
    else:
        tails += 1

print(f"\n--- Results ---")
print(f"Total flips : {n}")
print(f"Heads       : {heads} ({heads / n * 100:.1f}%)")
print(f"Tails       : {tails} ({tails / n * 100:.1f}%)")
