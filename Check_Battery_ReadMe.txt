# Check Battery README

## Overview

The provided code serves as a utility script that monitors the battery status of a computer. If the battery percentage drops below 20% and the computer is not plugged in, the program displays a warning to the user, prompting them to plug in their device.

## Prerequisites

To successfully run the script, ensure that you have:

- Python 3.8

- The `psutil` library installed. If not, you can install it using pip:

  ```bash
  pip install psutil
  ```

- `tkinter`, which comes pre-installed with most Python installations. If for any reason you don't have it, you can install it:

  - For Debian-based distributions:

    ```bash
    sudo apt-get install python3-tk
    ```

  - For Windows, `tkinter` should be available by default with Python.

## How to Use

1. Navigate to the directory containing the script.
2. Run the script using Python:

    ```bash
    Check_Battery.py
    ```

3. The script will check the battery status every 5 minutes by default. If the battery percentage is below 20% and the device is not plugged in, a pop-up warning will be displayed.

## Code Structure & Details

### Libraries Used

- `psutil`: Used to fetch battery details.
- `tkinter`: Used to create a GUI pop-up.
- `ctypes`: Used to bring the pop-up to the foreground.
- `time`: Used for the sleep functionality to set intervals between battery checks.

### Functions

- `check_battery()`: This function checks the battery status of the computer.

    - It uses `psutil.sensors_battery()` to get the battery status.
    - Checks if the battery percentage is less than 20% and if the device is not plugged in.
    - If the above condition is met, it displays a warning message using `tkinter.messagebox` and `ctypes.windll.user32.MessageBoxW` to ensure that the pop-up is visible in the foreground.

### Continuous Check

The script uses a `while True:` loop at the end to keep checking the battery status. By default, it checks every 5 minutes (`time.sleep(300)`). Adjusting the number `300` can change the check interval. E.g., for a 10-minute interval, use `time.sleep(600)`.

## Troubleshooting

1. If you encounter any error messages related to missing libraries, ensure you've installed all required prerequisites as mentioned in the 'Prerequisites' section.
2. If the pop-up does not come to the foreground, ensure that the script has the necessary permissions to display pop-ups.

---
