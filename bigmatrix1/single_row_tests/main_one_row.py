from machine import Pin
import neopixel
from font import font

# Matrix configuration
ROW_PINS = [16, 17, 19, 27, 33]  # Pins for each row
MATRIX_WIDTH = 96  # Width of each row
MATRIX_HEIGHT = len(ROW_PINS)  # Total number of rows
BRIGHTNESS = 1

# Initialize NeoPixel matrices for each row
matrices = [neopixel.NeoPixel(Pin(pin), MATRIX_WIDTH) for pin in ROW_PINS]

# Map matrix coordinates to LED index for vertical serpentine layout
def map_matrix(x, row_index):
    col = x
    if col % 2 == 0:  # Even column
        return row_index
    else:  # Odd column
        return MATRIX_HEIGHT - 1 - row_index

# Render a character on a specific row
def render_character_on_row(character, x_offset, color, row_index):
    char_data = font.get(character, [0] * 8)
    matrix = matrices[row_index]
    for x, row in enumerate(char_data):  # Loop through rows for vertical orientation
        for y in range(8):  # Each bit represents a pixel in the column
            if row & (1 << (7 - y)):  # Check each bit
                pixel_index = x + x_offset
                if pixel_index < MATRIX_WIDTH:
                    matrix[pixel_index] = (
                        int(color[0] * BRIGHTNESS),
                        int(color[1] * BRIGHTNESS),
                        int(color[2] * BRIGHTNESS),
                    )

# Render text on a specific row
def render_text_on_row(text, color, row_index):
    matrix = matrices[row_index]
    matrix.fill((0, 0, 0))  # Clear the row
    x_offset = 0
    for char in text:
        render_character_on_row(char, x_offset, color, row_index)
        x_offset += 8  # Move to the next character
        if x_offset >= MATRIX_WIDTH:
            break
    matrix.write()  # Update the row

# Main execution
render_text_on_row("HELLO", (127, 0, 0), 0)  # First row
render_text_on_row("WORLD", (0, 127, 0), 1)  # Second row
render_text_on_row("TEST", (0, 0, 127), 2)   # Third row
render_text_on_row("ROWS", (127, 127, 0), 3) # Fourth row
render_text_on_row("DONE", (127, 0, 127), 4) # Fifth row
