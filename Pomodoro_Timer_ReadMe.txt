---

# Pomodoro Timer

A simple, user-friendly desktop application built using Python and the tkinter library to implement the Pomodoro Technique.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation and Execution](#installation-and-execution)
4. [Features](#features)
5. [Customization](#customization)
6. [Acknowledgments](#acknowledgments)

## Introduction

The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique encourages people to work with the time they have, rather than against it. Using this method, you break your workday into 25-minute chunks (or "pomodoros") separated by five-minute breaks. This approach can enhance focus and concentration by providing regular restful pauses.

The `Pomodoro_Timer.py` script provides a convenient and intuitive way to apply the Pomodoro Technique using a graphical user interface.

## Requirements

1. Python 3.x
2. tkinter (usually comes bundled with Python)

## Installation and Execution

1. Make sure you have Python installed. You can check your current version by running:
    ```bash
    python --version
    ```

    OR 

    ```bash
    python3 --version
    ```

2. If tkinter is not installed (though it's usually included with Python), you can install it using pip:

    ```bash
    pip install tk
    ```

3. Clone the repository or download the `Pomodoro_Timer.py` script to your machine.

4. Navigate to the directory containing the script and run:

    ```bash
    python Pomodoro_Timer.py
    ```

    OR 

    ```bash
    python3 Pomodoro_Timer.py
    ```

## Features

1. **Interactive GUI**: The application provides a clear and concise graphical interface, showing the remaining time and allowing users to start the timer with a single click.

2. **Visual Feedback**: The timer display changes color based on the session type—green for work sessions, orange for short breaks, and red for long breaks.

3. **Notifications**: The application provides popup notifications to inform users when it's time to start working or take a break.

4. **Customizable Intervals**: Although set to the traditional 25-minute work, 5-minute short break, and 15-minute long break intervals, these durations can be easily customized in the script.

## Customization

To modify the default intervals:

1. Open the `Pomodoro_Timer.py` script in a text editor or IDE.
2. Locate the `PomodoroTimer` class instantiation at the bottom of the script.
3. Modify the parameters in the `PomodoroTimer` class initialization to set your desired work duration, short break duration, long break duration, and total cycles.

Example:

```python
timer = PomodoroTimer(work_duration=30, short_break_duration=10, long_break_duration=20, cycles=4)
```

This would set the work sessions to 30 minutes, short breaks to 10 minutes, long breaks to 20 minutes, and the total number of cycles to 4.

## Acknowledgments

* Thanks to Francesco Cirillo for the Pomodoro Technique concept.
* This script was inspired by the need to enhance productivity and focus in work-from-home environments.

---

