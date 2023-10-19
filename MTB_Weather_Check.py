import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
Summary:
--------
This script fetches the weather forecast for specified MTB (Mountain Biking) trails on the i90 Corridor
using the National Weather Service API. Based on the forecast, it determines whether it's favorable to ride
on the trails. The script then consolidates the forecast information and sends it as an email report to the 
specified recipients.
"""

# Send an email using the specified SMTP settings
def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Set up email headers and body
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = ', '.join(to_email)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attempt to send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Fetch the forecast data for the specified latitude and longitude from the National Weather Service
def fetch_forecast_data(lat, lon):
    # Construct the metadata URL
    metadata_url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(metadata_url)
    if response.status_code != 200:
        raise ValueError("Error fetching metadata")
    data = response.json()
    # Extract the forecast URL from the metadata
    forecast_url = data["properties"]["forecast"]
    response = requests.get(forecast_url)
    if response.status_code != 200:
        raise ValueError("Error fetching forecast data")
    # Return the forecast periods
    return response.json()["properties"]["periods"]

# Determine if it's favorable to ride based on the forecast
def determine_ride(forecast):
    forecast = forecast.lower()

    if "rain" in forecast:
        return "POSSIBLE RAIN"
    elif any(cond in forecast for cond in
             ["snow", "ice", "hail", "sleet", "storm", "thunderstorm", "tornado", "hurricane"]):
        return "NO RIDE (UNFAVORABLE WEATHER)"
    else:
        return "RIDE"

# Generate a detailed forecast report for the specified location
def generate_forecast_report(location_name, periods):
    weather_report = f"Weather Forecast for {location_name}:\n\n"
    day_summaries = []

    for period in periods[:7]:
        # Compile forecast details for each period
        weather_report += f"""
        Time: {period['startTime']} to {period['endTime']}
        Temperature: {period['temperature']}°F
        Forecast: {period['shortForecast']}
        Wind Speed: {period['windSpeed']}
        Wind Direction: {period['windDirection']}
        Detailed Weather: {period['detailedForecast']}
        """

        ride_status = determine_ride(period['shortForecast'])
        weather_report += f"{ride_status}\n\n"
        day_summaries.append({"day": period['name'], "status": ride_status})

    return weather_report, day_summaries

# Main execution
if __name__ == "__main__":
    # Define MTB trail locations with their respective latitude and longitude
    locations = [
        {"name": "Tiger Mountain, WA", "latitude": 47.488222, "longitude": -121.947280},
        {"name": "Raging Ridge, WA", "latitude": 47.479191, "longitude": -121.825460},
        {"name": "Duthie, WA", "latitude": 47.578293, "longitude": -121.978108},
        {"name": "Tokul, WA", "latitude": 47.569393, "longitude": -121.859686},
    ]

    combined_weather_report = ""
    all_summaries = []

    for location in locations:
        try:
            # Fetch forecast data for each location
            periods = fetch_forecast_data(location["latitude"], location["longitude"])
            # Generate report for each location
            report, day_summaries = generate_forecast_report(location["name"], periods)
            combined_weather_report += report
            all_summaries.append({"location": location['name'], "days": day_summaries})
        except Exception as e:
            print(f"Error fetching data for {location['name']}: {str(e)}")

    summary_section = "Summary Report:\n\n"
    for summary in all_summaries:
        favorable_days = [day['day'] for day in summary['days'] if day['status'] == 'RIDE']
        if favorable_days:
            days_string = ', '.join(favorable_days)
            summary_section += f"Favorable to ride at {summary['location']} on: {days_string}\n"
    summary_section += "\n---------------------------------------------\n\n"

    # Email setup
    subject = "Daily MTB Weather Forecast Report"
    intro_body = "Weather Report for Local MTB Trails on the i90 Corridor\n\n"
    outro_body = ("If you have any suggestions for this report, or would like to be removed from the distribution list "
                  "please reply to this email\n\n Thanks,\n\n Trabun Automation")

    to_email = ["", ""]  # Replace with the recipient's email addresses
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = ""  # Replace with your Gmail email address
    smtp_password = ""  # Replace with your Gmail password or an app-specific password

    # Send the consolidated report as an email
    send_email(subject, intro_body + summary_section + combined_weather_report + outro_body, to_email,
               smtp_server, smtp_port, smtp_username, smtp_password)
