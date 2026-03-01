# Project 11 — Calculator

**Difficulty:** Beginner
**Topics:** Functions, conditionals, `while` loops, `input()`, error handling

---

## What you're building

A menu-driven command-line calculator. The user picks an operation, enters two numbers, and sees the result. Keep going until they choose to quit.

---

## Requirements

1. Show a menu of operations:
   ```
   [1] Add
   [2] Subtract
   [3] Multiply
   [4] Divide
   [5] Quit
   ```
2. Ask for two numbers after the user picks an operation.
3. Print the result clearly (e.g., `12 + 7 = 19`).
4. Handle **division by zero** without crashing.
5. Handle **non-numeric input** without crashing.
6. Write each operation as its own **function**.

---

## Example Output

```
=== Calculator ===
[1] Add  [2] Subtract  [3] Multiply  [4] Divide  [5] Quit

Choose operation: 3
Enter first number: 6
Enter second number: 7
6.0 * 7.0 = 42.0

Choose operation: 4
Enter first number: 10
Enter second number: 0
Error: can't divide by zero!
```

---

## Stretch Goals

- [ ] Add **modulo** (`%`) and **exponentiation** (`**`) operations.
- [ ] Keep a **history** of calculations and let the user print it.
- [ ] Let the user chain operations: use the previous result as the first number.
- [ ] Add a `sqrt` option using the `math` module.

---

## Hints

- Store each operation as a function: `def add(a, b): return a + b`.
- Use a `dict` to map menu choices to functions: `ops = {"1": add, "2": subtract, ...}`.
- Wrap `float(input(...))` in a `try/except ValueError` block.
