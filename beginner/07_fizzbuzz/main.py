while True:
    try:
        n = int(input("Count up to: "))
        if n < 1:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a whole number.")

results = []
for i in range(1, n + 1):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    results.append(output if output else str(i))

print()
for i, value in enumerate(results):
    print(value, end="  ")
    if (i + 1) % 10 == 0:
        print()
print()
