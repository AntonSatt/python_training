import random

WORDS = [
    "python", "hangman", "keyboard", "bicycle", "elephant",
    "tornado", "library", "whisper", "blanket", "sunrise",
    "quantum", "jupiter", "mystery", "penguin", "shelter",
    "volcano", "rainbow", "dolphin", "captain", "lantern",
]

MAX_LIVES = 6


def play():
    word = random.choice(WORDS)
    guessed = set()
    lives = MAX_LIVES

    print(f"\nI've picked a word with {len(word)} letters. You have {MAX_LIVES} wrong guesses.\n")

    while lives > 0:
        display = " ".join(letter if letter in guessed else "_" for letter in word)
        wrong = sorted(g for g in guessed if g not in word)

        print(f"{display}    Lives: {lives}   Wrong guesses: {wrong}")

        if "_" not in display:
            print(f"\nYou got it! The word was '{word}'. Well done!")
            return

        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print(f"You already guessed '{guess}'.")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"Nice! '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"Nope! '{guess}' is not in the word.")

    print(f"\nGame over! The word was '{word}'.")


while True:
    play()
    again = input("\nPlay again? (y/n): ").lower().strip()
    if again != "y":
        print("Thanks for playing!")
        break
