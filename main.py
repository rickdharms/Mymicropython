import network
import time
from machine import Pin
import neopixel
from font import font

# Matrix configuration
MATRIX_WIDTH = 96
MATRIX_HEIGHT = 8  # Corrected height
PIN = 16  # Explicitly use pin 16 for the matrix
BRIGHTNESS = 1

# Initialize NeoPixel matrix
matrix = neopixel.NeoPixel(Pin(PIN), MATRIX_WIDTH * MATRIX_HEIGHT)

# WiFi credentials
SSID = "harmslosp"
PASSWORD = "Larisa!49"

'''
# Connect to WiFi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.5)
    print("Connected to WiFi:", wlan.ifconfig())
'''
# Map matrix coordinates to LED index for vertical serpentine layout
def map_matrix(x, y):
    col = MATRIX_WIDTH - 1 - x  # Reverse x for top-right start
    if col % 2 == 0:  # Even column
        return col * MATRIX_HEIGHT + y  # Keep y as is
    else:  # Odd column
        return col * MATRIX_HEIGHT + (MATRIX_HEIGHT - 1 - y)  # Reverse y for odd columns



# Render a character on the matrix for rotated vertical orientation
def render_character(character, x_offset, color):
    char_data = font.get(character, [0] * 8)
    for y, row in enumerate(char_data):  # Loop through rows for vertical orientation
        flipped_row = sum(
            (1 if (row >> bit) & 1 else 0) << (7 - bit) for bit in range(8)
        )  # Manual bit flipping
        for x in range(8):  # Each bit represents a pixel in the column
            if flipped_row & (1 << (7 - x)):  # Check each bit in the flipped row
                index = map_matrix(x + x_offset, y)
                if index < len(matrix):  # Bounds check
                    matrix[index] = (
                        int(color[0] * BRIGHTNESS),
                        int(color[1] * BRIGHTNESS),
                        int(color[2] * BRIGHTNESS),
                    )

# Render text on the matrix
def render_text(text, color):
    matrix.fill((0, 0, 0))  # Clear the matrix
    x_offset = 0
    reversed_text = ''.join(reversed(text))  # Manually reverse the text
    for char in reversed_text:
        render_character(char, x_offset, color)
        x_offset += 8  # Fixed character width
        if x_offset >= MATRIX_WIDTH:
            break
    matrix.write()
'''
matrix.fill((127, 127, 127))  # Set all LEDs to white
matrix.write()
print("Matrix test complete.")
'''

# Main execution
#connect_to_wifi()
render_text("! < > # , .", (127, 0, 0))

