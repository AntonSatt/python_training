# Project 03 — Todo List CLI

**Difficulty:** Beginner–Intermediate
**Topics:** Lists, dicts, `json`, file I/O, functions, a simple menu loop

---

## What you're building

A command-line todo list app that **saves your tasks to a file** so they survive between runs. You'll build a small menu-driven interface to add, view, complete, and delete tasks.

---

## Requirements

1. On startup, **load** existing tasks from a `tasks.json` file (or start fresh if it doesn't exist).
2. Show a menu:
   ```
   [1] View tasks
   [2] Add task
   [3] Mark task complete
   [4] Delete task
   [5] Quit
   ```
3. Each task should have at least: `id`, `title`, `done` (bool).
4. On quit (or after every change), **save** the tasks back to `tasks.json`.
5. Split your code into **functions** — one per action.

---

## Example Output

```
[1] View tasks
[2] Add task
> 2

Task title: Buy oat milk
Task added!

[1] View tasks
> 1

  [ ] 1. Buy oat milk
  [x] 2. Learn Python again
```

---

## Stretch Goals

- [ ] Add a **due date** field and sort tasks by date.
- [ ] Add a **priority** (low / medium / high) and color-code them with ANSI codes.
- [ ] Support filtering: show only incomplete tasks.
- [ ] Accept command-line arguments with `sys.argv` so you can do `python todo.py add "Buy milk"`.

---

## Hints

- `json.load(f)` and `json.dump(data, f, indent=2)` handle reading/writing JSON.
- Use `enumerate()` when printing a numbered list of tasks.
