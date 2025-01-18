import tkinter as tk
from tkinter import messagebox, colorchooser
import paho.mqtt.client as mqtt
import json
import time

# MQTT Configuration
MQTT_BROKER = "10.0.0.46"
MQTT_TOPIC = "led_matrix/command"

# MQTT Client Setup
client = mqtt.Client()

# Callback for disconnection
def on_disconnect(client, userdata, rc):
    """Handle disconnection and attempt to reconnect."""
    print("Disconnected from MQTT broker. Attempting to reconnect...")
    while True:
        try:
            client.reconnect()
            print("Reconnected to MQTT broker.")
            break
        except Exception as e:
            print(f"Reconnect failed: {e}")
            time.sleep(5)  # Retry every 5 seconds

# MQTT Client Setup
#client = mqtt.Client()

# Add disconnect handler
client.on_disconnect = on_disconnect

# Connect to MQTT broker
try:
    client.connect(MQTT_BROKER)
    client.loop_start()
except Exception as e:
    print(f"Error connecting to MQTT broker: {e}")

# GUI Functions
def send_command():
    """Send command to the MQTT broker."""
    try:
        row = int(row_var.get()) - 1  # Adjust row to match 0-based indexing
        if row < 0 or row > 4:
            raise ValueError("Row must be between 1 and 5.")

        text = text_var.get()
        color = color_var.get()
        if not text and not clear_row_var.get() and not clear_matrix_var.get():
            raise ValueError("Please provide text or select a clear option.")

        # Decode Unicode escape sequences
        text = text.encode().decode('unicode_escape')

        r, g, b = [int(c) for c in color.strip("()").split(",")]
        command = {
            "row": row,
            "text": text,
            "color": [r, g, b],
        }

        if clear_row_var.get():
            command["text"] = ""
            clear_row_var.set(False)  # Automatically uncheck the "Clear Row" box

        if clear_matrix_var.get():
            command = {
                "row": -1,  # Special row for clearing the matrix
                "text": "",
                "color": [0, 0, 0],
            }
            clear_matrix_var.set(False)  # Automatically uncheck "Clear Matrix"

        # Debug print for the payload
        print(f"Sending command: {json.dumps(command, ensure_ascii=False)}")

        client.publish(MQTT_TOPIC, json.dumps(command, ensure_ascii=False))
        feedback_var.set("Command sent successfully!")
    except Exception as e:
        feedback_var.set(f"Error: {e}")
      
def choose_color():
    """Open a color chooser dialog and set the selected color."""
    color_code = colorchooser.askcolor(title="Choose text color")[0]
    if color_code:
        color_var.set(f"({int(color_code[0])}, {int(color_code[1])}, {int(color_code[2])})")

def reset_inputs():
    """Reset all inputs to their default state."""
    row_var.set("")
    text_var.set("")
    color_var.set("(255, 255, 255)")
    clear_row_var.set(False)
    clear_matrix_var.set(False)
    feedback_var.set("Inputs reset.")

# GUI Setup
root = tk.Tk()
root.title("LED Matrix Controller")

# Row Selection
tk.Label(root, text="Row (1-5):").grid(row=0, column=0, sticky="e")
row_var = tk.StringVar()
tk.Entry(root, textvariable=row_var).grid(row=0, column=1)

# Text Entry
tk.Label(root, text="Text:").grid(row=1, column=0, sticky="e")
text_var = tk.StringVar()
tk.Entry(root, textvariable=text_var).grid(row=1, column=1)

# Color Selection
tk.Label(root, text="Color (RGB):").grid(row=2, column=0, sticky="e")
color_var = tk.StringVar(value="(255, 255, 255)")
tk.Entry(root, textvariable=color_var).grid(row=2, column=1)
tk.Button(root, text="Choose Color", command=choose_color).grid(row=2, column=2)

# Clear Row Checkbox
clear_row_var = tk.BooleanVar()
tk.Checkbutton(root, text="Clear Row", variable=clear_row_var).grid(row=3, column=0, columnspan=2, sticky="w")

# Clear Matrix Checkbox
clear_matrix_var = tk.BooleanVar()
tk.Checkbutton(root, text="Clear Matrix", variable=clear_matrix_var).grid(row=3, column=2)

# Submit Button
tk.Button(root, text="Submit", command=send_command).grid(row=4, column=0, columnspan=2)

# Reset Inputs Button
tk.Button(root, text="Reset Inputs", command=reset_inputs).grid(row=4, column=2)

# Feedback Label
feedback_var = tk.StringVar()
feedback_label = tk.Label(root, textvariable=feedback_var, fg="green")
feedback_label.grid(row=5, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()
