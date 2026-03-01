# Project 10 — Mini URL Shortener

**Difficulty:** Advanced
**Topics:** Flask, REST API design, JSON storage, `hashlib`/`random`, redirects

---

## What you're building

A fully working URL shortener — your own mini bit.ly. A small Flask web server that accepts long URLs, returns short codes, and redirects anyone who visits the short link. First real web server project!

---

## Setup

```
pip install flask
```

---

## Requirements

Build a Flask app with these endpoints:

| Method | Route | What it does |
|---|---|---|
| `POST` | `/shorten` | Accepts `{"url": "https://..."}`, returns `{"short": "http://localhost:5000/abc123"}` |
| `GET` | `/<code>` | Redirects to the original URL (or 404 if code unknown) |
| `GET` | `/stats/<code>` | Returns the original URL + how many times it's been visited |
| `GET` | `/all` | Returns all stored short links |

**Storage:** Save links to a `links.json` file (no database needed).

**Short codes:** Generate a random 6-character alphanumeric string (e.g., `k7Xp2Q`).

---

## Example Usage (via curl or a REST client)

```bash
# Shorten a URL
curl -X POST http://localhost:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://docs.python.org/3/"}'

# Response:
{"short": "http://localhost:5000/aB3xY9", "code": "aB3xY9"}

# Visit the short link (in browser or curl -L):
curl -L http://localhost:5000/aB3xY9
# → redirects to https://docs.python.org/3/

# Check stats:
curl http://localhost:5000/stats/aB3xY9
# → {"url": "https://docs.python.org/3/", "visits": 3}
```

---

## Stretch Goals

- [ ] Build a simple **HTML frontend** — a form where you paste a URL and get the short link back.
- [ ] Let users supply a **custom alias**: `POST /shorten {"url": "...", "alias": "my-docs"}`.
- [ ] Add **expiry** — links expire after N days, configurable per link.
- [ ] Validate that submitted URLs are actually valid URLs before storing them.
- [ ] Switch storage from JSON to **SQLite** using Python's built-in `sqlite3`.
- [ ] Add a `DELETE /<code>` endpoint.

---

## Hints

- `flask.redirect(url, 302)` is all you need for the redirect endpoint.
- Generate a code with: `''.join(random.choices(string.ascii_letters + string.digits, k=6))`
- Load/save JSON at the start/end of each request, or use a global dict and persist on writes.
- Test everything with `curl` or install a REST client like [Insomnia](https://insomnia.rest/) or [Bruno](https://www.usebruno.com/).
- Run your dev server with: `flask --app app.py run --debug`
