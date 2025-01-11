from machine import Pin
import neopixel

# Matrix configuration
ROW_PINS = [16, 17, 19, 27, 33]  # Pins for each row
MATRIX_WIDTH = 96  # Horizontal columns
MATRIX_HEIGHT = 8  # Vertical pixels per column
TOTAL_LEDS = MATRIX_WIDTH * MATRIX_HEIGHT  # Total LEDs per row

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize NeoPixel matrices for all rows
matrices = [neopixel.NeoPixel(Pin(pin), TOTAL_LEDS) for pin in ROW_PINS]

# Map matrix coordinates to LED index for vertical serpentine layout
def map_matrix(x, y):
    col = x
    if col % 2 == 0:  # Even column
        return col * MATRIX_HEIGHT + y
    else:  # Odd column
        return col * MATRIX_HEIGHT + (MATRIX_HEIGHT - 1 - y)  # Reverse y for odd columns

# Clear a specific row
def clear_row(row_index):
    matrix = matrices[row_index]
    matrix.fill((0, 0, 0))
    matrix.write()

# Clear all rows
def clear_all():
    for matrix in matrices:
        matrix.fill((0, 0, 0))
        matrix.write()

# Draw stripes
def draw_stripes():
    stripe_height = 4  # Height of each stripe in pixels
    for y in range(MATRIX_HEIGHT * len(ROW_PINS)):
        color = RED if (y // stripe_height) % 2 == 0 else WHITE
        row_index = y // MATRIX_HEIGHT
        matrix_y = y % MATRIX_HEIGHT
        if row_index < len(matrices):
            for x in range(MATRIX_WIDTH):
                index = map_matrix(x, matrix_y)
                matrices[row_index][index] = color
            matrices[row_index].write()

# Draw blue field
def draw_blue_field():
    blue_width = 38  # Blue field width (40% of MATRIX_WIDTH)
    blue_height = 20  # Blue field height in pixels
    for y in range(blue_height):
        row_index = y // MATRIX_HEIGHT
        matrix_y = y % MATRIX_HEIGHT
        if row_index < len(matrices):
            for x in range(blue_width):
                index = map_matrix(x, matrix_y)
                matrices[row_index][index] = BLUE
            matrices[row_index].write()

# Draw stars
def draw_stars():
    star_rows = 9  # Rows of stars
    star_cols = 11  # Columns of stars
    star_spacing_x = 3  # Horizontal spacing between stars
    star_spacing_y = 2  # Vertical spacing between stars
    blue_width = 38
    for row in range(star_rows):
        for col in range(star_cols):
            if (row + col) % 2 == 0:  # Staggered pattern
                x = col * star_spacing_x
                y = row * star_spacing_y
                if x < blue_width and y < 20:  # Confine stars to the blue field
                    row_index = y // MATRIX_HEIGHT
                    matrix_y = y % MATRIX_HEIGHT
                    index = map_matrix(x, matrix_y)
                    matrices[row_index][index] = WHITE
                    matrices[row_index].write()

# Main execution: Render the American flag
def render_american_flag():
    clear_all()
    draw_stripes()
    draw_blue_field()
    draw_stars()

render_american_flag()
