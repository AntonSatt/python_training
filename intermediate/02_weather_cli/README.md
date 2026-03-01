# Project 05 — Weather CLI

**Difficulty:** Intermediate
**Topics:** `requests`, REST APIs, JSON parsing, `argparse`, error handling

---

## What you're building

A command-line app that fetches real weather data for any city and displays it nicely in the terminal. Your first taste of working with a real-world API!

---

## Setup

1. Sign up for a **free** API key at [https://openweathermap.org/api](https://openweathermap.org/api) (the free tier is plenty).
2. Store your key in a `.env` file (never hard-code secrets!):
   ```
   OWM_API_KEY=your_key_here
   ```
3. Install dependencies:
   ```
   pip install requests python-dotenv
   ```

---

## Requirements

1. Accept a city name as a command-line argument:
   ```
   python weather.py "Copenhagen"
   ```
2. Call the OpenWeatherMap **Current Weather** endpoint.
3. Display:
   - City & country
   - Temperature (°C or °F — let the user choose)
   - "Feels like" temperature
   - Weather description (e.g., "light rain")
   - Humidity & wind speed
4. Handle errors gracefully (city not found, no internet, bad API key).

---

## Example Output

```
Weather in Copenhagen, DK
--------------------------
  Clear sky
  Temp:       8°C (feels like 5°C)
  Humidity:   72%
  Wind:       4.5 m/s
```

---

## Stretch Goals

- [ ] Add a **5-day forecast** using the forecast endpoint.
- [ ] Show a weather emoji based on the condition (☀️ 🌧️ ❄️ etc.).
- [ ] Cache the last result to a file so it works offline and shows "Last updated: X min ago".
- [ ] Accept a **zip code** or **lat/lon** in addition to city names.

---

## Hints

- Load your `.env` with `from dotenv import load_dotenv; load_dotenv()`, then `os.getenv("OWM_API_KEY")`.
- `response.raise_for_status()` will throw an exception for 4xx/5xx HTTP errors — great for error handling.
- The API returns temperature in Kelvin by default; pass `&units=metric` for Celsius.
