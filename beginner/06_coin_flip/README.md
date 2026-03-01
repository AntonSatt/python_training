# Project 12 — Coin Flip Simulator

**Difficulty:** Beginner
**Topics:** `random`, `while` loops, basic stats, f-strings, `input()`

---

## What you're building

A coin flip simulator! Flip a coin as many times as you like, watch the results accumulate, and see statistics at the end — a gentle intro to probability.

---

## Requirements

1. Ask the user how many times to flip the coin (or let them flip one at a time).
2. Randomly land on **Heads** or **Tails** for each flip.
3. Print the result of each flip.
4. After all flips, print a summary:
   - Total flips
   - Number of Heads and Tails
   - Percentage of each
5. Handle non-numeric or invalid input gracefully.

---

## Example Output

```
How many times should I flip the coin? 5

Flip 1: Heads
Flip 2: Tails
Flip 3: Heads
Flip 4: Heads
Flip 5: Tails

--- Results ---
Total flips : 5
Heads       : 3 (60.0%)
Tails       : 2 (40.0%)
```

---

## Stretch Goals

- [ ] Let the user flip coins **one at a time** by pressing Enter, and show a running tally after each flip.
- [ ] Simulate a **streak tracker** — report the longest consecutive run of Heads or Tails.
- [ ] Flip 10 000 times and plot the running percentage converging to 50% (use `matplotlib`).
- [ ] Add a **weighted coin** mode where the user can set the probability of heads.

---

## Hints

- `random.choice(["Heads", "Tails"])` picks one at random.
- Use f-strings to format the percentage: `f"{heads / total * 100:.1f}%"`.
- A simple counter variable for heads is all the state you need.
