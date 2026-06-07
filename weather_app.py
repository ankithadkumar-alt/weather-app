import requests   # to call the API
import json       # to read the response

# ── YOUR API KEY ──────────────────────────────────────────────────────────────
# Get your free key from: https://openweathermap.org/api
# Sign up → go to "API Keys" tab → copy the key → paste it below
API_KEY = "your_api_key_here"   # <-- replace this

# ── API URL ───────────────────────────────────────────────────────────────────
# This is the OpenWeatherMap endpoint we will call.
# We pass the city name, our API key, and units=metric to get Celsius.
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ── FUNCTION: Fetch weather data ──────────────────────────────────────────────

def get_weather(city_name):
    """Call the OpenWeatherMap API and return the weather data for a city."""

    # Build the parameters to send with the request
    params = {
        "q":     city_name,   # city name the user typed
        "appid": API_KEY,     # our API key
        "units": "metric",    # metric = Celsius, imperial = Fahrenheit
    }

    try:
        # Make the GET request to the API
        response = requests.get(BASE_URL, params=params)

        # Check if the request was successful (status code 200 = OK)
        if response.status_code == 200:
            # Parse the JSON response into a Python dictionary
            data = response.json()
            return data

        elif response.status_code == 404:
            print(f"\n  City '{city_name}' not found. Please check the spelling.")
            return None

        elif response.status_code == 401:
            print("\n  Invalid API key. Please check your API_KEY in the script.")
            return None

        else:
            print(f"\n  Error: Received status code {response.status_code}")
            return None

    except requests.exceptions.ConnectionError:
        print("\n  No internet connection. Please check your network.")
        return None

    except Exception as error:
        print(f"\n  Something went wrong: {error}")
        return None


# ── FUNCTION: Display weather results ─────────────────────────────────────────

def display_weather(data, city_name):
    """Print the weather data in a clean, readable format."""

    # Pull out the values we need from the JSON dictionary
    temperature   = data["main"]["temp"]          # current temperature
    feels_like    = data["main"]["feels_like"]    # what it feels like
    humidity      = data["main"]["humidity"]      # humidity percentage
    description   = data["weather"][0]["description"]  # e.g. "light rain"
    wind_speed    = data["wind"]["speed"]         # wind speed in m/s
    country       = data["sys"]["country"]        # country code e.g. IN
    min_temp      = data["main"]["temp_min"]      # min temperature today
    max_temp      = data["main"]["temp_max"]      # max temperature today

    # Print everything neatly
    print("\n" + "=" * 45)
    print(f"  Weather in {city_name.title()}, {country}")
    print("=" * 45)
    print(f"  Condition    : {description.title()}")
    print(f"  Temperature  : {temperature}°C  (feels like {feels_like}°C)")
    print(f"  Min / Max    : {min_temp}°C  /  {max_temp}°C")
    print(f"  Humidity     : {humidity}%")
    print(f"  Wind Speed   : {wind_speed} m/s")
    print("=" * 45)


# ── FUNCTION: Filter / compare multiple cities ─────────────────────────────────

def compare_cities(cities):
    """Fetch weather for multiple cities and show them side by side."""

    print("\n" + "=" * 65)
    print(f"  {'City':<20} {'Temp (°C)':<14} {'Humidity':<12} {'Condition'}")
    print("=" * 65)

    for city in cities:
        data = get_weather(city)
        if data:
            temp      = data["main"]["temp"]
            humidity  = data["main"]["humidity"]
            condition = data["weather"][0]["description"].title()
            country   = data["sys"]["country"]
            print(f"  {city.title() + ', ' + country:<20} {str(temp) + '°C':<14} {str(humidity) + '%':<12} {condition}")

    print("=" * 65)


# ── MAIN: Ask user what they want to do ───────────────────────────────────────

def main():
    print("\n" + "=" * 45)
    print("   Weather App — InternSpark Task 2")
    print("=" * 45)

    print("\nWhat do you want to do?")
    print("  [1]  Search weather for one city")
    print("  [2]  Compare weather across multiple cities")
    print("  [0]  Exit")

    choice = input("\n  Your choice: ").strip()

    if choice == "1":
        city = input("  Enter city name: ").strip()
        if city:
            data = get_weather(city)
            if data:
                display_weather(data, city)
        else:
            print("  Please enter a city name.")

    elif choice == "2":
        raw = input("  Enter city names separated by commas (e.g. London, Tokyo, Mumbai): ").strip()
        cities = [c.strip() for c in raw.split(",") if c.strip()]
        if cities:
            compare_cities(cities)
        else:
            print("  Please enter at least one city.")

    elif choice == "0":
        print("  Bye!")

    else:
        print("  Invalid choice. Please enter 0, 1, or 2.")


if __name__ == "__main__":
    main()
