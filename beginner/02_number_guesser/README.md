# Project 02 — Number Guesser

**Difficulty:** Beginner
**Topics:** `random`, `while` loops, conditionals, type conversion

---

## What you're building

The computer picks a secret number between 1 and 100. You have to guess it. After each guess the game tells you "too high", "too low", or "you got it!" — and tracks how many tries it took.

---

## Requirements

1. Use `random.randint(1, 100)` to pick the secret number.
2. Keep prompting the user until they guess correctly.
3. After each wrong guess print whether the answer is **higher** or **lower**.
4. When they win, print how many guesses it took.
5. Handle bad input (e.g., if they type "abc" instead of a number) without crashing.

---

## Example Output

```
I've picked a number between 1 and 100. Can you guess it?

Guess: 50
Too low!

Guess: 75
Too high!

Guess: 63
You got it in 3 guesses!
```

---

## Stretch Goals

- [ ] Add difficulty levels: Easy (1–20), Medium (1–100), Hard (1–1000).
- [ ] Give the user a limited number of guesses (e.g., 7) — classic binary search territory.
- [ ] After the game ends, show the optimal number of guesses needed (hint: it's `log2(range)`).
- [ ] Let the computer guess YOUR number using binary search — flip the roles!

---

## Hints

- `int(input(...))` converts the user's text to an integer — wrap it in a `try/except` block.
- A `while True:` loop with a `break` when the user wins is a clean pattern here.
