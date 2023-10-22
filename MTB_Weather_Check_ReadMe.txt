MTB_Weather_Check_ReadMe.txt
----------

MTB Weather Forecast Reporter
=============================

Table of Contents:
------------------
1. Overview
2. Dependencies
3. File Structure
4. Detailed Functional Descriptions
5. Configuration & Setup
6. Usage
7. Best Practices & Recommendations
8. Future Enhancements
9. Troubleshooting
10. Author & Contact
11. Disclaimer

1. Overview
-----------
The MTB Weather Forecast Reporter is designed to aid MTB enthusiasts by automating the weather forecast retrieval for specific MTB trails along the i90 Corridor. It then provides a quick recommendation regarding whether the trail is rideable based on weather conditions. 

2. Dependencies:
----------------
- Python 3.x
- `requests`: To make HTTP requests.
- Standard Python libraries for email: `smtplib`, `email.mime.multipart`, and `email.mime.text`.

3. File Structure:
------------------
- `MTB_Weather_Check.py`: Main script (or replace with your script name).

4. Detailed Functional Descriptions:
-----------------------------------
- `send_email(...)`: Establishes a connection to the SMTP server and sends the consolidated weather report.
- `fetch_forecast_data(...)`: Interacts with the National Weather Service API to obtain the weather forecast.
- `determine_ride(...)`: A logic function to assess the weather's impact on rideability.
- `generate_forecast_report(...)`: Organizes and formats the forecast into a readable format.
- Main block: Coordinates the functionalities, creating a streamlined process from data retrieval to email dispatch.

5. Configuration & Setup:
-------------------------
- Edit the script and input the recipient email addresses in the `to_email` list.
- Populate `smtp_username` and `smtp_password` with the appropriate email credentials.

6. Usage:
---------
Run the script using:

python MTB_Weather_Check.py

7. Best Practices & Recommendations:
-----------------------------------
- Do not hard-code sensitive information like SMTP credentials. Instead, use environment variables or a separate configuration file.
- If using Gmail, either enable "Less Secure App Access" (not recommended for main accounts) or utilize app-specific passwords.
- It may be beneficial to incorporate logging for better error diagnostics.

8. Future Enhancements:
-----------------------
- Expand to more MTB trail locations or integrate with an external database of locations.
- Incorporate user feedback mechanisms to refine the weather-rideability logic.
- Provide an option to fetch forecasts for different time periods (e.g., 3-day, 7-day, 14-day).
- 3 Day Precipitation report

9. Troubleshooting:
-------------------
- "SMTP Authentication Error": Ensure you've input the correct credentials or app-specific password. Also, check the "Less Secure App Access" setting.
- "Error fetching data": Check your internet connection. If the issue persists, the API endpoint might have changed or is temporarily down.

10. Author & Contact:
---------------------
Matthew Trabun

11. Disclaimer:
---------------
The script is a supplementary tool. Always consult professional sources or local authorities for urgent weather updates. The script's recommendations are based on general conditions and may not account for sudden weather changes or specific trail conditions.

