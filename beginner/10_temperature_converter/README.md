# Project 16 — Temperature Converter

**Difficulty:** Beginner
**Topics:** Functions, math, conditionals, `while` loops, `input()`

---

## What you're building

A handy temperature conversion tool that converts between Celsius, Fahrenheit, and Kelvin. Each conversion lives in its own function, and a menu lets the user convert as many temperatures as they like.

---

## Requirements

1. Write separate functions for each conversion:
   - `celsius_to_fahrenheit(c)`
   - `fahrenheit_to_celsius(f)`
   - `celsius_to_kelvin(c)`
   - `kelvin_to_celsius(k)`
   - `fahrenheit_to_kelvin(f)`
   - `kelvin_to_fahrenheit(k)`
2. Show a menu and let the user pick a conversion.
3. Ask for the input temperature and print the result rounded to **2 decimal places**.
4. Loop until the user chooses to quit.
5. Reject temperatures below **absolute zero** (−273.15°C / 0 K).

---

## Example Output

```
Temperature Converter
[1] °C → °F   [2] °F → °C
[3] °C → K    [4] K  → °C
[5] °F → K    [6] K  → °F
[7] Quit

Choose: 1
Enter temperature in °C: 100
100°C = 212.00°F

Choose: 4
Enter temperature in K: -5
Error: temperature cannot be below absolute zero (0 K).
```

---

## Stretch Goals

- [ ] Accept the temperature and unit as **command-line arguments** and print all three scales at once.
- [ ] Add **Rankine** as a fourth scale.
- [ ] Show a fun context clue for the result (e.g., "That's the boiling point of water!" for 100°C).
- [ ] Build a conversion **table** — print a range of values in two scales side by side.

---

## Hints

- Formulas:
  - °C → °F: `(c * 9/5) + 32`
  - °F → °C: `(f - 32) * 5/9`
  - °C → K:  `c + 273.15`
- `round(value, 2)` rounds to 2 decimal places.
- Absolute zero check: after converting any input to Celsius, make sure it's ≥ −273.15.
