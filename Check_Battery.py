import psutil
import tkinter as tk
from tkinter import messagebox
import ctypes
import time

# Function to check the battery status
def check_battery():
    try:
        # Get battery status
        battery = psutil.sensors_battery()

        if battery is None:
            raise RuntimeError("Unable to get battery status")

        plugged = battery.power_plugged

        # Check if battery percentage is below 20% and not plugged in
        if battery.percent < 20 and not plugged:
            # Create a pop-up window
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            messagebox.showinfo("Battery Alert", "Battery is below 20%. Please plug inS.")
            ctypes.windll.user32.MessageBoxW(0, "Battery is below 20%. Please plug in or close this dialog.",
                                             "Battery Alert", 0x40 | 0x1)  # Bring the pop-up to the foreground

    except Exception as e:
        # Handle any exceptions and display an error message
        print(f"An error occurred: {e}")


# Check the battery status every 5 minutes (you can adjust the interval)
while True:
    check_battery()
    time.sleep(300)  # Sleep for 300 seconds (5 minutes)
