# Project 06 — Text Adventure Engine

**Difficulty:** Intermediate
**Topics:** Classes, OOP, dicts, game loops, multiple files

---

## What you're building

A small text-based adventure game where the player explores rooms, picks up items, and solves a simple puzzle to win. The real goal here is designing a clean class structure — rooms, items, and a player.

---

## Requirements

Build at least these classes:

| Class | Responsibility |
|---|---|
| `Room` | Has a name, description, exits (N/S/E/W), and a list of items |
| `Item` | Has a name and description |
| `Player` | Has a current room, an inventory, and methods to move/pick up/use items |
| `Game` | The main loop — reads input, calls the right methods, checks win condition |

**Map (minimum):**
- 5 connected rooms (e.g., entrance hall, library, dungeon, garden, tower).
- 3 items to find (e.g., a key, a torch, a note).
- A locked door that requires the key — finding and using it wins the game.

**Commands to support:**
```
go north / go n
look
take <item>
inventory / inv
use <item>
help
quit
```

---

## Example Output

```
=== The Forgotten Tower ===

You are in the Entrance Hall.
A dusty corridor stretches before you. Cobwebs hang from every corner.
Exits: north, east
Items here: rusty key

> take rusty key
You pick up the rusty key.

> go north
You are in the Library...
```

---

## Stretch Goals

- [ ] Load the map from a `map.json` file instead of hard-coding it.
- [ ] Add a health system and an enemy that moves between rooms.
- [ ] Add save/load game state using `json`.
- [ ] Add riddles — the player must answer correctly to pass a room.

---

## Hints

- Store exits as a dict: `{"north": room_object, "east": other_room}`.
- Parse input with `.split()` — `cmd = input("> ").lower().split()` gives you `["go", "north"]`.
- Keep the game loop in `Game.run()` and call `self.player.move(direction)` etc.
