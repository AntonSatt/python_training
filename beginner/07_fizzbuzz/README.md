# Project 13 — FizzBuzz Challenge

**Difficulty:** Beginner
**Topics:** Loops, conditionals, modulo `%`, `input()`, type conversion

---

## What you're building

The legendary FizzBuzz — a classic coding interview warm-up. Print numbers 1 to N, but replace multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz". Then make it interactive with custom rules.

---

## Requirements

1. Ask the user for a number `N`.
2. Print every number from 1 to N, applying the rules:
   - Multiple of 3 → `Fizz`
   - Multiple of 5 → `Buzz`
   - Multiple of both → `FizzBuzz`
   - Otherwise → the number itself
3. After the basic version works, ask the user for **custom words and divisors**:
   - "Replace multiples of ___ with ___"
   - Support up to **3 custom rules** at once.
4. Handle non-numeric or out-of-range input gracefully.

---

## Example Output

```
Count up to: 20

1  2  Fizz  4  Buzz  Fizz  7  8  Fizz  Buzz
11  Fizz  13  14  FizzBuzz  16  17  Fizz  19  Buzz
```

Custom mode:
```
Divisor: 4   Word: Zap
Divisor: 7   Word: Pop

1  2  3  Zap  5  6  Pop  Zap  9  10  11  Zap  13  Pop  15  Zap  ...
```

---

## Stretch Goals

- [ ] Print the output in a grid (e.g., 10 values per row) instead of a single long line.
- [ ] Count how many Fizzes, Buzzes, and FizzBuzzes occurred and show a summary.
- [ ] Let the user play an **interactive version**: the computer counts, the user must shout "Fizz/Buzz" at the right moments or lose a life.
- [ ] Accept `N` as a command-line argument with `sys.argv`.

---

## Hints

- Check the combined condition first: `if n % 3 == 0 and n % 5 == 0`.
- For custom rules, store them as a list of `(divisor, word)` tuples.
- `print(value, end="  ")` lets you print multiple things on the same line with spacing.
