# Project 17 — Hangman

**Difficulty:** Beginner–Intermediate
**Topics:** Strings, lists, `while` loops, sets, functions

---

## What you're building

The classic word-guessing game! The program picks a secret word, you guess one letter at a time, and a stick-figure gallows grows with each wrong guess. Get the word before you run out of lives.

---

## Requirements

1. Store a list of at least **20 words** to pick from at random.
2. Display the word as underscores: `_ _ _ _ _` with correctly guessed letters filled in.
3. The player gets **6 wrong guesses** before losing.
4. After each guess:
   - Show the updated word display.
   - Show which letters have been guessed (wrong guesses highlighted).
   - Show remaining lives.
5. Handle edge cases: repeated guesses, non-letter input, multi-character input.
6. When the game ends, reveal the full word and ask if the player wants to play again.

---

## Example Output

```
_ _ _ _ _ _ _    Lives: 6   Wrong guesses: []

Guess a letter: e
Nice! 'e' is in the word.

_ _ _ e _ _ e    Lives: 6   Wrong guesses: []

Guess a letter: z
Nope! 'z' is not in the word.

_ _ _ e _ _ e    Lives: 5   Wrong guesses: [z]
```

---

## Stretch Goals

- [ ] Draw an ASCII hangman figure that grows with each wrong guess.
- [ ] Add **difficulty levels** that control word length or number of lives.
- [ ] Load words from a text file instead of a hard-coded list.
- [ ] Add a **hint** command that reveals one letter at the cost of a life.

---

## Hints

- Store guessed letters in a `set` — checking membership with `in` is fast and sets ignore duplicates.
- To display the word: `" ".join(letter if letter in guessed else "_" for letter in word)`.
- A `while` loop with conditions `lives > 0` and `"_" in display` keeps the game going.
- Use `word.lower()` and `guess.lower()` so case doesn't matter.
