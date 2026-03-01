# Project 15 — Word Counter

**Difficulty:** Beginner
**Topics:** Strings, dicts, `input()`, sorting, basic text processing

---

## What you're building

A tool that analyses a block of text and tells you everything about it: word count, character count, most common words, and more. Text analysis is a gateway skill to data science and NLP.

---

## Requirements

1. Ask the user to paste or type a block of text (hint: read until a blank line or use `sys.stdin`).
2. Count and display:
   - Total **words**
   - Total **characters** (with and without spaces)
   - Total **sentences** (count `.`, `!`, and `?`)
   - Total **unique words** (case-insensitive)
3. Show the **top 5 most common words** (ignore common stop words like "the", "a", "is", "in", "of").
4. The stop word list should be a variable at the top of your file — easy to customise.

---

## Example Output

```
Paste your text (press Enter twice when done):
To be or not to be that is the question whether tis nobler
in the mind to suffer the slings and arrows of outrageous fortune

--- Analysis ---
Words          : 28
Characters     : 148 (122 without spaces)
Sentences      : 0
Unique words   : 21

Top 5 words:
  1. be       — 2
  2. nobler   — 1
  3. mind     — 1
  4. suffer   — 1
  5. slings   — 1
```

---

## Stretch Goals

- [ ] Accept a **filename** as input instead of typed text: `python counter.py my_essay.txt`.
- [ ] Calculate **average word length**.
- [ ] Find the **longest word** in the text.
- [ ] Output the full word frequency table sorted alphabetically.

---

## Hints

- `text.lower().split()` gives you a list of words (it splits on whitespace).
- Strip punctuation from words with `word.strip(".,!?;:\"")`  before counting.
- A `dict` is perfect for counting: `counts[word] = counts.get(word, 0) + 1`.
- Sort by count: `sorted(counts.items(), key=lambda x: x[1], reverse=True)`.
