# Import required modules
import time
import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    # Initialize the properties and GUI components of the Pomodoro timer
    def __init__(self, work_duration=25, short_break_duration=5, long_break_duration=15, cycles=4):
        # Convert the durations from minutes to seconds
        self.work_duration = work_duration * 60
        self.short_break_duration = short_break_duration * 60
        self.long_break_duration = long_break_duration * 60
        self.cycles = cycles  # Total number of work cycles
        self.cycle_count = 0  # Counter for the number of completed work cycles

        # Set up the main GUI window
        self.root = tk.Tk()
        self.root.title("Pomodoro Timer")

        # Create and pack the label to display the timer countdown
        self.label = tk.Label(self.root, font=('sans', 20))
        self.label.pack(pady=20)

        # Create and pack the start button, and link it to the start_timer method
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack()

    # Method to update the countdown display on the GUI
    def update_display(self, remaining_time):
        mins, secs = divmod(remaining_time, 60)  # Convert seconds into minutes and seconds
        self.label.config(text=f"{mins:02d}:{secs:02d}")  # Update label text with the formatted time

    # Method for the countdown logic; it updates every second
    def countdown(self, duration):
        for remaining_time in range(duration, -1, -1):  # Count from the duration down to 0
            self.update_display(remaining_time)
            self.root.update()  # Update the GUI window
            time.sleep(1)  # Pause for one second

    # Method to start the Pomodoro timer cycles
    def start_timer(self):
        for _ in range(self.cycles):
            self.label.config(fg="green")  # Set the display color to green during work time
            self.countdown(self.work_duration)  # Start work countdown
            self.cycle_count += 1  # Increment the cycle count after work session

            # Check if it's time for a short or long break
            if self.cycle_count == self.cycles:
                self.label.config(fg="red")  # Set display color to red for a long break
                messagebox.showinfo("Pomodoro Timer", "Work cycles completed! Taking a long break...")
                self.countdown(self.long_break_duration)
            else:
                self.label.config(fg="orange")  # Set display color to orange for a short break
                messagebox.showinfo("Pomodoro Timer", "Taking a short break...")
                self.countdown(self.short_break_duration)
        
        # Show a message box when all cycles are done
        messagebox.showinfo("Pomodoro Timer", "Pomodoro cycles completed! Well done!")
        
    # Method to keep the GUI window running
    def run(self):
        self.root.mainloop()

# The main execution point of the script
if __name__ == "__main__":
    timer = PomodoroTimer()  # Create an instance of the PomodoroTimer class
    timer.run()  # Start the GUI event loop
