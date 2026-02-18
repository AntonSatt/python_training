# Project 01 — Mad Libs Generator

**Difficulty:** Beginner
**Topics:** `input()`, strings, f-strings

---

## What you're building

A classic Mad Libs game! Ask the user for random words (a noun, a verb, an adjective, etc.) without telling them the story, then plug them into a funny template and reveal the result.

---

## Requirements

1. Ask the user for at least **8 words** of different types:
   - 2 nouns
   - 2 verbs (past tense)
   - 2 adjectives
   - 1 place
   - 1 name
2. Store each answer in a variable.
3. Print the completed story using an **f-string** (or `.format()`).

---

## Example Output

```
Enter a noun: banana
Enter a verb (past tense): exploded
Enter an adjective: fluffy
...

--- YOUR STORY ---
Once upon a time, a fluffy banana exploded in the middle of Paris...
```

---

## Stretch Goals

- [ ] Store multiple story templates in a list and pick one at random.
- [ ] Let the user play again without restarting the script.
- [ ] Add color to the output using ANSI escape codes (e.g., `\033[92m`).

---

## Hints

- `input("Enter a noun: ")` prompts the user and returns their answer as a string.
- f-strings look like this: `f"The {adjective} {noun} {verb}."` — super clean!
