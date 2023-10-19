import requests

# Summary: This script retrieves and prints the weather forecast for a specified location,
# including temperature, short forecast, wind speed, wind direction, and detailed weather description.
# It also checks if it's raining for each forecast period and provides a relevant message.

def get_weather_forecast(location_name, lat, lon):
    # Step 1: Retrieve metadata
    metadata_url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(metadata_url)

    # Check if the metadata retrieval was successful
    if response.status_code != 200:
        print(f"Error: Unable to retrieve metadata for {location_name}.")
        return

    # Extract metadata JSON data
    data = response.json()
    forecast_url = data["properties"]["forecast"]

    # Step 2: Retrieve weather forecast data
    response = requests.get(forecast_url)

    # Check if the weather forecast retrieval was successful
    if response.status_code != 200:
        print(f"Error: Unable to retrieve weather forecast for {location_name}.")
        return

    # Extract weather forecast JSON data
    forecast_data = response.json()

    # Step 3: Extract and print weather information for each period
    periods = forecast_data["properties"]["periods"]

    # Print the header with the location name
    print(f"Weather Forecast for {location_name}:\n")

    for period in periods:
        print(f"Time: {period['startTime']} to {period['endTime']}")
        print(f"Temperature: {period['temperature']}°F")
        print(f"Forecast: {period['shortForecast']}")
        print(f"Wind Speed: {period['windSpeed']}")
        print(f"Wind Direction: {period['windDirection']}")
        print(f"Detailed Weather: {period['detailedForecast']}")

        # Check if it's raining for the current period
        is_raining = "rain" in period['shortForecast'].lower()

        # Print a message based on whether it's raining or not
        if is_raining:
            print("It's raining. Look for potential weather windows.")
        else:
            print("It's not raining. It's a good time to ride a bike!")

        # Add a separator for readability
        print("---------------\n")

if __name__ == "__main__":
    # Location: Issaquah, Washington
    location_name = "Issaquah, WA"
    latitude = 47.5301
    longitude = -122.0326

    # Call the function with the specified location
    get_weather_forecast(location_name, latitude, longitude)
