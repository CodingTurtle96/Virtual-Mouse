import tkinter as tk
from tkinter import *
import subprocess

def start_program():
    global process
    process = subprocess.Popen(["python", "Virtual Mouse prototype-V2.py"])

def stop_program():
    global process
    if process:
        process.terminate()  # Terminate the subprocess if it exists
    else:
        messagebox.showwarning("Warning", "No program running.")

def close_program():
    root.destroy()  # Close the main window

# Create the main window
root = tk.Tk()
root.title("Virtual mouse")

# Set the dimensions of the window
window_width = 270
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

start_button = tk.Button(root, text="ON Mouse", command=start_program)
start_button.grid(row = 3, column = 1,pady = 10, padx = 100)

stop_button = tk.Button(root, text="OFF Mouse", command=stop_program)
stop_button.grid(row = 4, column = 1, pady = 10, padx = 100)

close_button = tk.Button(root, text="Close", command=close_program)
close_button.grid(row = 5, column = 1                                                                                                                                                                                                                                                                                                    , pady = 10, padx = 100)

Label(root,text='Air Cursor').grid(row=1,column=1)

# Initialize process variable
process = None

# Run the main event loop
root.mainloop()
