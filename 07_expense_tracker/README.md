# Project 07 — Expense Tracker

**Difficulty:** Intermediate–Advanced
**Topics:** `csv`/`json`, `datetime`, data aggregation, `argparse`, formatted table output

---

## What you're building

A personal finance CLI tool. Log expenses, categorize them, and get a monthly summary showing where your money went. A practical tool you might actually use!

---

## Requirements

1. Store expenses in a `expenses.csv` (or `.json`) file with columns:
   `date, amount, category, description`

2. Support these subcommands via `argparse`:
   ```
   python expenses.py add 45.50 food "Dinner at Thai place"
   python expenses.py list
   python expenses.py summary
   python expenses.py summary --month 2026-02
   ```

3. `list` shows a formatted table of all expenses.
4. `summary` shows total spent per **category** and a grand total.
5. `summary --month YYYY-MM` filters to that month only.

---

## Example Output

```
$ python expenses.py summary --month 2026-02

Summary for February 2026
--------------------------
  Food          247.50 kr
  Transport      89.00 kr
  Entertainment  55.00 kr
--------------------------
  TOTAL         391.50 kr
```

---

## Stretch Goals

- [ ] Set a **monthly budget** per category and warn when you're over.
- [ ] Export a summary to a nicely formatted **markdown** or **HTML** file.
- [ ] Add a `delete <id>` command.
- [ ] Plot spending by category as a bar chart using `matplotlib`.
- [ ] Calculate and show average daily spend for the month.

---

## Hints

- Use Python's `csv` module (`csv.DictReader` / `csv.DictWriter`) for easy column-by-column access.
- `datetime.datetime.strptime(date_str, "%Y-%m-%d")` parses date strings.
- Build the summary by iterating expenses and using a `dict` to accumulate totals per category.
- For a nice table, look at the `tabulate` library: `pip install tabulate`.
