# Project 18 — Number Inspector

**Difficulty:** Beginner
**Topics:** Math, functions, conditionals, loops, `input()`

---

## What you're building

A tool that takes any positive integer and tells you fascinating things about it — whether it's prime, a perfect number, a palindrome, and more. A fun way to practice writing focused, single-purpose functions.

---

## Requirements

Write a function for each of these checks and call them all on the user's number:

| Check | Description |
|---|---|
| **Prime** | Only divisible by 1 and itself |
| **Perfect** | Equals the sum of its proper divisors (e.g., 6 = 1+2+3) |
| **Armstrong** | Sum of its digits each raised to the power of the digit count (e.g., 153 = 1³+5³+3³) |
| **Palindrome** | Reads the same forwards and backwards (e.g., 121) |
| **Even/Odd** | Divisible by 2 or not |
| **Factors** | List all factors of the number |

Print a neat summary with all results. Loop so the user can check multiple numbers.

---

## Example Output

```
Enter a number (or 'q' to quit): 153

Inspecting 153...
  Even/Odd   : Odd
  Prime      : No
  Perfect    : No
  Armstrong  : Yes! (1³ + 5³ + 3³ = 153)
  Palindrome : Yes
  Factors    : 1, 3, 9, 17, 51, 153

Enter a number (or 'q' to quit): 28

Inspecting 28...
  Even/Odd   : Even
  Prime      : No
  Perfect    : Yes! (1 + 2 + 4 + 7 + 14 = 28)
  Armstrong  : No
  Palindrome : No
  Factors    : 1, 2, 4, 7, 14, 28
```

---

## Stretch Goals

- [ ] Add a **Fibonacci check** — is this number in the Fibonacci sequence?
- [ ] Add a **Happy Number check** (repeatedly sum the squares of digits; if you reach 1, it's happy).
- [ ] Accept a **range** of numbers and list which ones satisfy a chosen property.
- [ ] Show how many steps the **Collatz conjecture** takes to reach 1 for the given number.

---

## Hints

- Prime check: try dividing by every number from 2 up to `int(n**0.5) + 1`.
- Proper divisors: all factors of `n` excluding `n` itself.
- Armstrong: `digits = [int(d) for d in str(n)]`, then sum `d ** len(digits) for d in digits`.
- Palindrome: `str(n) == str(n)[::-1]`.
