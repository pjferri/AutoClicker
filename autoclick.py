import time
import pyautogui
import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title("Autoclicker")

# Create a label for the interval input
interval_label = tk.Label(window, text="Time Between Clicks (S)")
interval_label.pack()

# Create an input field for the interval
interval_input = tk.Entry(window)
interval_input.pack()

# Create a label for the number of clicks
clicks_label = tk.Label(window, text="Number of clicks")
clicks_label.pack()

# Create an input field for the number of clicks
clicks_input = tk.Entry(window)
clicks_input.pack()

# Create a start button
start_button = tk.Button(window, text="Start")
start_button.pack()

# Create a stop button
stop_button = tk.Button(window, text="Stop")
stop_button.pack()

# Flag to track whether the autoclicker is running
is_running = False

# Function to start the autoclicker
def start_clicking():
    # Get the interval and number of clicks from the input fields
    interval = float(interval_input.get())
    num_clicks = int(clicks_input.get())

    # Set the is_running flag to True
    global is_running
    is_running = True

    # Loop and click the mouse repeatedly
    for i in range(num_clicks):
        pyautogui.click()
        time.sleep(interval)

        # Stop clicking if the is_running flag is set to False
        if not is_running:
            break

# Function to stop the autoclicker
def stop_clicking():
    # Set the is_running flag to False
    global is_running
    is_running = False

# Set the start button's command to start the autoclicker
start_button["command"] = start_clicking

# Set the stop button's command to stop the autoclicker
stop_button["command"] = stop_clicking

# Start the Tkinter event loop
window.mainloop()