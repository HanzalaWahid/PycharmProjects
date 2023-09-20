import requests
import json

while True:
    city = input("Enter your City: \n")
    if city.lower() == "quit":
        break
    url = f"http://api.weatherapi.com/v1/current.json?key=75c1801719d44264b48185934231509&q={city}"

    try:
        r = requests.get(url)

        if r.status_code == 200:
            data = r.json()
            temperature_celsius = data["current"]["temp_c"]
            temperature_fahrenheit = data["current"]["temp_f"]
            condition = data["current"]["condition"]["text"]
            print(f"Temperature in {city}: {temperature_celsius}°C / {temperature_fahrenheit}°F / Condition: {condition}")
        else:
            print(f"Failed to retrieve data. Status code: {r.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError as e:
        print(f"Error: {e}. Data format may have changed.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
