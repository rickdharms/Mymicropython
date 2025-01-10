from machine import Pin
import neopixel
from font import font

# Matrix configuration
ROW_PINS = [16, 17, 19, 27, 33]  # Pins for each row
MATRIX_WIDTH = 96  # Horizontal columns
MATRIX_HEIGHT = 8  # Vertical pixels per column
TOTAL_LEDS = MATRIX_WIDTH * MATRIX_HEIGHT  # Total LEDs per row

# Initialize NeoPixel matrices for all rows
matrices = [neopixel.NeoPixel(Pin(pin), TOTAL_LEDS) for pin in ROW_PINS]

# Map matrix coordinates to LED index for vertical serpentine layout
def map_matrix(x, y):
    col = x  # Flip column direction to correct mirror effect
    if col % 2 == 0:  # Even column
        return col * MATRIX_HEIGHT + y
    else:  # Odd column
        return col * MATRIX_HEIGHT + (MATRIX_HEIGHT - 1 - y)  # Reverse y for odd columns

# Render a character on a specific row
def render_character(character, x_offset, color, matrix):
    char_data = font.get(character, [0] * 8)
    for y, row in enumerate(char_data):
        for x in range(8):
            if row & (1 << (7 - x)):  # Check each bit
                index = map_matrix(x + x_offset, y)
                if 0 <= index < len(matrix):  # Bounds check
                    matrix[index] = (
                        int(color[0]),
                        int(color[1]),
                        int(color[2]),
                    )

# Render text on a specific row
def render_text_on_row(text, color, row_index):
    matrix = matrices[row_index]
    matrix.fill((0, 0, 0))  # Clear the row
    x_offset = 0  # Start at the left
    for char in text:
        render_character(char, x_offset, color, matrix)
        x_offset += 8  # Move to the next character
        if x_offset >= MATRIX_WIDTH:  # Prevent overflow
            break
    matrix.write()

# Main execution: Display text on all rows
render_text_on_row("Hello", (0, 0, 127), 0)  # Row 0: Blue
render_text_on_row("World", (0, 127, 0), 1)  # Row 1: Green
render_text_on_row("I am Happy", (127, 0, 0), 2)      # Row 2: Red
render_text_on_row("\u2190,\u2192", (0, 0, 127), 3)     # Row 3: Blue
render_text_on_row("\u2191,\u2193,\u2713", (127, 127, 127), 4)  # Row 4: White
