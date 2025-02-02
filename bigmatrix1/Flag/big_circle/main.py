from machine import Pin
import neopixel
import math

# Matrix configuration
ROW_PINS = [16, 17, 19, 27, 33]  # Pins for each row
MATRIX_WIDTH = 96  # Horizontal columns
MATRIX_HEIGHT = 8  # Vertical pixels per column
TOTAL_LEDS = MATRIX_WIDTH * MATRIX_HEIGHT  # Total LEDs per row

# Colors
RED = (125, 0, 0)
WHITE = (125, 125, 125)
BLUE = (0, 0, 125)

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
'''
# Draw circle of 13 stars
def draw_circle_of_stars():
    circle_center_x = 19  # Center of the circle in the blue field
    circle_center_y = 10  # Center of the circle in the blue field
    circle_radius = 6  # Radius of the circle
    num_stars = 13  # Number of stars in the circle
    for i in range(num_stars):
        angle = 2 * math.pi * i / num_stars
        x = int(circle_center_x + circle_radius * math.cos(angle))
        y = int(circle_center_y + circle_radius * math.sin(angle))
        if 0 <= x < 38 and 0 <= y < 20:  # Confine stars to the blue field
            row_index = y // MATRIX_HEIGHT
            matrix_y = y % MATRIX_HEIGHT
            index = map_matrix(x, matrix_y)
            matrices[row_index][index] = WHITE
            matrices[row_index].write()
'''
# Draw a larger circle of 13 stars with 4-pixel stars
def draw_circle_of_stars():
    circle_center_x = 19  # Center of the circle in the blue field
    circle_center_y = 10  # Center of the circle in the blue field
    circle_radius = 8  # Larger radius for the circle
    num_stars = 13  # Number of stars in the circle

    for i in range(num_stars):
        angle = 2 * math.pi * i / num_stars
        x = int(circle_center_x + circle_radius * math.cos(angle))
        y = int(circle_center_y + circle_radius * math.sin(angle))

        if 0 <= x < 38 and 0 <= y < 20:  # Confine stars to the blue field
            draw_star(x, y)

# Draw a single 2x2 star
def draw_star(center_x, center_y):
    offsets = [(-1, -1), (-1, 0), (0, -1), (0, 0)]  # 2x2 grid offsets
    for dx, dy in offsets:
        x = center_x + dx
        y = center_y + dy
        if 0 <= x < 38 and 0 <= y < 20:  # Bounds check within blue field
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
    draw_circle_of_stars()

render_american_flag()
