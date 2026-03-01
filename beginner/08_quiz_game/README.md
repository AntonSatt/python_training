# Project 14 — Quiz Game

**Difficulty:** Beginner
**Topics:** Lists, dicts, `for` loops, score tracking, `random`

---

## What you're building

A multiple-choice trivia quiz! The program asks questions one by one, the user picks an answer, and at the end they get a score with a rating. A great excuse to learn how Python stores structured data.

---

## Requirements

1. Store at least **8 questions** in a list of dicts, each with:
   - `"question"` — the question text
   - `"options"` — a list of 4 answer choices (A–D)
   - `"answer"` — the correct option letter (`"A"`, `"B"`, `"C"`, or `"D"`)
2. Present each question with numbered options.
3. Accept the user's answer (case-insensitive) and tell them if they're right or wrong.
4. Track the score.
5. After all questions, print the final score and a rating:
   - 8/8 → "Perfect score!"
   - 6–7 → "Great job!"
   - 4–5 → "Not bad!"
   - Below 4 → "Keep studying!"
6. Shuffle the question order each run using `random.shuffle()`.

---

## Example Output

```
Question 1/8:
What is the capital of Japan?
  A) Beijing
  B) Seoul
  C) Tokyo
  D) Bangkok

Your answer: c
Correct!

...

You scored 6 out of 8 — Great job!
```

---

## Stretch Goals

- [ ] Load questions from a `questions.json` file so you can add more without changing the code.
- [ ] Also shuffle the **answer options** each run (and update the correct answer key accordingly).
- [ ] Add a **timer** — each question must be answered within 10 seconds.
- [ ] Track which questions the user got wrong and offer a **review mode** at the end.

---

## Hints

- A list of dicts is the natural structure: `questions = [{"question": "...", "options": [...], "answer": "A"}, ...]`.
- `user_input.strip().upper()` normalises the user's input before comparing.
- `random.shuffle(questions)` shuffles in place — no need to reassign.
