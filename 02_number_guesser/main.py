# Guessing game!

import random


def get_number():
    while True:
        try:
            return(int(input("Guess: ")))
        except ValueError:
            print("That is not a valid number.")


def main():
    random_num = random.randint(1, 100)
    tries = 0

    print("I've picked a number between 1 and 100. Can you guess it?")

    while True:
        tries += 1
        test_num = get_number()
        if test_num < random_num:
            print("Higher")
        elif test_num > random_num:
            print("Lower")
        else:
            break

    print(f"Well done! You found {random_num} in {tries} tries!!")

if __name__ == "__main__":
    main()
