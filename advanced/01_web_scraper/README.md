# Project 08 — Web Scraper

**Difficulty:** Advanced
**Topics:** `requests`, `BeautifulSoup`, HTML parsing, `csv`, rate limiting, ethics

---

## What you're building

A web scraper that pulls structured data from a website and saves it to a CSV. You'll learn to navigate HTML, extract data, and be a responsible scraper.

---

## Pick one of these target sites (all scraping-friendly):

| Site | What to scrape |
|---|---|
| `books.toscrape.com` | Book titles, prices, ratings, availability |
| `quotes.toscrape.com` | Quotes, authors, tags |
| `news.ycombinator.com` | HN front page: title, URL, points, comments |

---

## Requirements

1. Install dependencies:
   ```
   pip install requests beautifulsoup4
   ```
2. Fetch and parse the **first 3 pages** of results (handle pagination).
3. Extract the relevant fields for your chosen target.
4. Save results to `output.csv`.
5. Add a **1-second delay** between requests (`time.sleep(1)`) — be a polite scraper.
6. Handle HTTP errors and missing fields without crashing.

---

## Example Output (`books.toscrape.com`)

```
title,price,rating,available
A Light in the Attic,£51.77,Three,True
Tipping the Velvet,£53.74,One,True
...
```

---

## Stretch Goals

- [ ] Add CLI flags to choose how many pages to scrape.
- [ ] De-duplicate results (in case you run the script twice).
- [ ] Scrape **detail pages** too — follow each book's link for its full description.
- [ ] Use `concurrent.futures` to fetch multiple pages in parallel (carefully!).
- [ ] Store data in SQLite instead of CSV using Python's built-in `sqlite3`.

---

## Hints

- `soup.select("article.product_pod")` uses CSS selectors — much cleaner than chained `.find()` calls.
- Always check `robots.txt` before scraping a real site.
- The `rating` on books.toscrape is a CSS class name ("Three"), not a number — you'll need to map it.
- Use `response.raise_for_status()` to catch HTTP errors early.
