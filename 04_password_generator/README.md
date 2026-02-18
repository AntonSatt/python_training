# Project 04 — Password Generator

**Difficulty:** Intermediate
**Topics:** `random`, `string`, `argparse`, functions, list comprehensions

---

## What you're building

A handy command-line tool that generates strong, random passwords. The user controls the length and which character types to include. Bonus: rate the strength of a user-supplied password.

---

## Requirements

1. Generate a password with configurable:
   - **Length** (default: 16)
   - Include/exclude **uppercase** letters
   - Include/exclude **digits**
   - Include/exclude **symbols** (`!@#$%^&*` etc.)
2. Use `argparse` so the user can run it like:
   ```
   python password_gen.py --length 20 --no-symbols
   ```
3. Print the generated password clearly.
4. Add a **strength checker** mode: the user passes in a password and your script rates it (Weak / Fair / Strong / Very Strong).

---

## Example Output

```
$ python password_gen.py --length 24
Generated password: kR7@mXp!2vNqL#dW9zYc&tJs

$ python password_gen.py --check "hello123"
Password strength: Weak (no uppercase, no symbols)
```

---

## Stretch Goals

- [ ] Generate **multiple** passwords at once (`--count 5`).
- [ ] Add a **memorable** mode that builds a passphrase from random words (e.g., `purple-rocket-lake-7!`).
- [ ] Copy the password to the clipboard using the `pyperclip` library.
- [ ] Avoid ambiguous characters (`0`, `O`, `1`, `l`) with a `--no-ambiguous` flag.

---

## Hints

- `string.ascii_letters`, `string.digits`, `string.punctuation` give you character pools.
- `random.shuffle(list)` then `''.join(list)` is a great pattern for mixing character types.
- The strength checker can check length + presence of each character type to build a score.
