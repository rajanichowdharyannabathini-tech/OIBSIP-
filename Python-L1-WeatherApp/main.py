import requests

# Add your OpenWeatherMap API Key here
API_KEY = "def79010d0070f1b12cbcceae4bdc948"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    # Input validation
    if not city.strip():
        print("Error: City name cannot be empty.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # API request
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        # Error handling
        if response.status_code == 404:
            print("Error: City not found.")
            return

        if response.status_code == 401:
            print("Error: Invalid API Key.")
            return

        response.raise_for_status()

        # Convert response into JSON
        weather_data = response.json()

        # Extract weather details
        city_name = weather_data["name"]
        temperature_c = weather_data["main"]["temp"]
        temperature_f = (temperature_c * 9/5) + 32
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]

        # Display weather information
        print("\n========== WEATHER REPORT ==========")
        print("City:", city_name)
        print(f"Temperature: {temperature_c} °C")
        print(f"Temperature: {temperature_f:.2f} °F")
        print(f"Humidity: {humidity}%")
        print("Weather Condition:", description.title())
        print(f"Wind Speed: {wind_speed} m/s")
        print("====================================")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Network connection failed.")

    except requests.exceptions.RequestException:
        print("Error: Unable to fetch weather data.")

    except Exception as error:
        print("Unexpected Error:", error)


# Main program
city = input("Enter city name: ")

get_weather(city)