# Project 10 — Rock Paper Scissors

**Difficulty:** Beginner
**Topics:** `random`, conditionals, `while` loops, score tracking

---

## What you're building

The classic hand game against the computer! The computer picks its move randomly, you pick yours, and the game decides who wins. Keep score across multiple rounds.

---

## Requirements

1. Let the user enter `rock`, `paper`, or `scissors` (or `q` to quit).
2. Use `random.choice()` to pick the computer's move.
3. Print both moves and announce the round winner.
4. Keep a running tally of **wins, losses, and draws**.
5. When the user quits, print the final score.
6. Reject invalid input and prompt again.

---

## Example Output

```
Rock, Paper, Scissors! (or 'q' to quit)

Your move: rock
Computer chose: scissors
You win!  ✓

Your move: paper
Computer chose: paper
It's a draw!

Your move: q

Final Score — You: 1 | Computer: 0 | Draws: 1
```

---

## Stretch Goals

- [ ] Add a best-of-N mode (e.g., first to 3 wins takes the match).
- [ ] Expand to **Rock Paper Scissors Lizard Spock** (5 options).
- [ ] Show a win-rate percentage at the end.
- [ ] Accept single-letter shortcuts: `r`, `p`, `s`.

---

## Hints

- Store valid choices in a list: `choices = ["rock", "paper", "scissors"]`.
- A nested `if/elif` or a dict of winning matchups handles the logic cleanly.
- `random.choice(choices)` picks a random element from the list.
