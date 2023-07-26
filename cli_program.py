import requests

def get_weather_by_date(date):
    url = "http://127.0.0.1:5000/weather"
    params = {"date": date}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data.get("temperature")
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred while fetching weather data: {e}")
        return None

def get_wind_speed_by_date(date):
    url = "http://127.0.0.1:5000/weather"
    params = {"date": date}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data.get("wind", {}).get("speed")
        else:
            print(f"Failed to fetch wind speed data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred while fetching wind speed data: {e}")
        return None

def get_pressure_by_date(date):
    url = "http://127.0.0.1:5000/weather"
    params = {"date": date}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data.get("pressure")
        else:
            print(f"Failed to fetch pressure data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred while fetching pressure data: {e}")
        return None

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_by_date(date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} K")
            else:
                print("Data not found for the given date.")

        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not found for the given date.")

        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not found for the given date.")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
