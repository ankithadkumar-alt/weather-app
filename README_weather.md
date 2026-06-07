# Weather App — Python API Integration

Fetches live weather data from OpenWeatherMap API and displays it in a clean format. Built for the InternSpark Python API Integration task.

---

## What it does

- Searches live weather for any city in the world
- Shows temperature, humidity, wind speed, and conditions
- Compares weather across multiple cities side by side

---

## Requirements

- Python 3.8+
- requests module (`pip install requests`)
- Free OpenWeatherMap API key

---

## Setup — Get your free API key (2 minutes)

1. Go to https://openweathermap.org/api
2. Click **Sign Up** — it's free
3. After signing in, go to **API Keys** tab
4. Copy the key shown there
5. Open `weather_app.py` and replace `your_api_key_here` with your key

---

## How to run

```
pip install requests
python weather_app.py
```

---

## Sample output

**Option 1 — Single city search:**
```
What do you want to do?
  [1]  Search weather for one city
  [2]  Compare weather across multiple cities

  Your choice: 1
  Enter city name: Mumbai

=============================================
  Weather in Mumbai, IN
=============================================
  Condition    : Haze
  Temperature  : 32.4°C  (feels like 38.1°C)
  Min / Max    : 31.0°C  /  33.0°C
  Humidity     : 74%
  Wind Speed   : 3.6 m/s
=============================================
```

**Option 2 — Compare cities:**
```
  Your choice: 2
  Enter city names: London, Tokyo, Mumbai

=================================================================
  City                 Temp (°C)      Humidity     Condition
=================================================================
  London, GB           18.2°C         65%          Partly Cloudy
  Tokyo, JP            27.5°C         80%          Light Rain
  Mumbai, IN           32.4°C         74%          Haze
=================================================================
```

---

## Python concepts used

- `requests` module — GET request to the API
- JSON parsing — `response.json()` converts API response to a Python dictionary
- `try/except` — handles connection errors and invalid city names
- `input()` — user types city name and menu choice
- Filter/search — user can search one city or compare many
- Status code handling — 200 OK, 404 not found, 401 invalid key

---

## Project structure

```
weather-app/
├── weather_app.py    ← main script
└── README.md
```
