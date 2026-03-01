# Project 19 — Countdown Timer

**Difficulty:** Beginner
**Topics:** `time` module, `while` loops, `input()`, string formatting, `os`

---

## What you're building

A terminal countdown timer. The user sets the time, and the display counts down second-by-second, updating in place. When it hits zero it rings an alert. Simple, satisfying, and genuinely useful.

---

## Requirements

1. Ask the user for the timer duration in **minutes and seconds** (or just seconds).
2. Count down one second at a time, updating the display on the **same line** (no scrolling).
3. When the timer reaches 0:
   - Print a clear "Time's up!" message.
   - Ring the terminal bell (`\a` or `print("\a")`).
4. Handle invalid input (negative numbers, non-integers) gracefully.
5. Let the user start another timer after one finishes (loop until they quit).

---

## Example Output

```
Set timer — Minutes: 1   Seconds: 30

  ⏱  01:29 remaining...
```
*(the display rewrites the same line as each second passes)*

```
  ⏱  00:00 remaining...

🔔 Time's up!

Set another timer? (y/n):
```

---

## Stretch Goals

- [ ] Accept the time directly as a command-line argument: `python timer.py 5:30`.
- [ ] Play a sequence of short beeps instead of a single bell (use `\a` multiple times with `time.sleep(0.3)`).
- [ ] Add a **stopwatch mode** that counts up instead of down.
- [ ] Show a simple ASCII **progress bar** that drains as time runs out.

---

## Hints

- `time.sleep(1)` pauses the program for one second.
- Print on the same line with `\r` (carriage return): `print(f"\r  ⏱  {display}", end="", flush=True)`.
- Format seconds as MM:SS: `f"{minutes:02d}:{seconds:02d}"`.
- `total_seconds = minutes * 60 + seconds` then decrement each loop.
