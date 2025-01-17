from machine import Pin
import neopixel
import network
from umqtt.simple import MQTTClient
import json
import socket
import struct
import time
from bigfont import bigfont

# WiFi Configuration
WIFI_SSID = "harmslosp"
WIFI_PASSWORD = "Larisa!49"

# MQTT Configuration
MQTT_BROKER = "10.0.0.46"  # Broker IP
MQTT_PORT = 1883
MQTT_TOPIC = "led_matrix/command"

# Matrix Configuration
ROW_PINS = [16, 17, 19, 27, 33]  # GPIO pins for each row
MATRIX_WIDTH = 96  # Horizontal columns
MATRIX_HEIGHT = 8  # Vertical pixels per column
TOTAL_LEDS = MATRIX_WIDTH * MATRIX_HEIGHT  # Total LEDs per row

# Initialize NeoPixel matrices for all rows
matrices = [neopixel.NeoPixel(Pin(pin), TOTAL_LEDS) for pin in ROW_PINS]

# Connect to WiFi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Connecting to WiFi...")
    while not wlan.isconnected():
        time.sleep(1)
    print(f"Connected to WiFi, IP address: {wlan.ifconfig()[0]}")

# Fetch current time from an NTP server
def get_ntp_time(host="pool.ntp.org"):
    """Fetch the current time from an NTP server."""
    NTP_DELTA = 2208988800  # Time difference between 1900 and 1970 (in seconds)
    try:
        addr = socket.getaddrinfo(host, 123)[0][-1]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        msg = b'\x1b' + 47 * b'\0'
        s.sendto(msg, addr)
        msg, _ = s.recvfrom(48)
        s.close()
        t = struct.unpack("!I", msg[40:44])[0]
        print(f"Raw NTP timestamp: {t}")
        unix_timestamp = t - NTP_DELTA
        print(f"Unix timestamp: {unix_timestamp}")
        return unix_timestamp
    except Exception as e:
        print(f"Error fetching NTP time: {e}")
        return None

def calculate_date_from_days(days):
    """Calculate the year, month, and day from days since the Unix epoch."""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1970
    while days >= 365 + is_leap_year(year):
        days -= 365 + is_leap_year(year)
        year += 1

    # Adjust for leap years
    days_in_month[1] = 29 if is_leap_year(year) else 28

    # Calculate month and day
    month = 1
    while days >= days_in_month[month - 1]:
        days -= days_in_month[month - 1]
        month += 1

    return year, month, days + 1

def is_leap_year(year):
    """Determine if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_dst():
    """Always return False for now (DST calculation is optional)."""
    return False

def replace_reserved_words(text):
    """Replace reserved words with dynamic values."""
    timestamp = get_ntp_time()
    if timestamp is None:
        print("NTP fetch failed. Returning original text.")
        return text  # If NTP fails, leave text as-is
    
    # Correctly convert timestamp to date and time components
    timestamp += -7 * 3600 if is_dst() else -8 * 3600  # Adjust for Pacific Time

    days_since_epoch = timestamp // 86400
    seconds_in_day = timestamp % 86400

    # Calculate date
    year, month, day = calculate_date_from_days(days_since_epoch)

    # Calculate time
    hour = (seconds_in_day // 3600) % 24
    minute = (seconds_in_day % 3600) // 60
    second = seconds_in_day % 60

    print(f"Calculated Date: {year}-{month:02}-{day:02}, Time: {hour:02}:{minute:02}:{second:02}")

    # Replace reserved words
    replacements = {
        "#DATE": f"{day:02}/{month:02}/{year}",
        "#TIME1": f"{hour:02}:{minute:02}",
        "#TIME2": f"{hour % 12 or 12:02}:{minute:02} {'AM' if hour < 12 else 'PM'}",
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    print(f"Replaced text: {text}")
    return text

# Map matrix coordinates to LED index for vertical serpentine layout
def map_matrix(x, y):
    col = x
    if col % 2 == 0:  # Even column
        return col * MATRIX_HEIGHT + y
    else:  # Odd column
        return col * MATRIX_HEIGHT + (MATRIX_HEIGHT - 1 - y)  # Reverse y for odd columns

# Render a character on a specific row
def render_character(character, x_offset, color, matrix):
    """Render a single character on the matrix."""
    char_data = bigfont.get(character, [0] * 8)  # Default: empty character
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
    """Render a line of text on a specific row."""
    matrix = matrices[row_index]
    matrix.fill((0, 0, 0))  # Clear the row
    x_offset = 0  # Start at the left
    for char in text:
        render_character(char, x_offset, color, matrix)
        x_offset += 8  # Move to the next character
        if x_offset >= MATRIX_WIDTH:  # Prevent overflow
            break
    matrix.write()

# MQTT Callback for incoming messages
def on_message(topic, msg):
    try:
        print(f"Received message on topic {topic}: {msg}")
        command = json.loads(msg.decode())  # Parse JSON payload

        row = command.get("row", None)
        text = command.get("text", "")
        color = command.get("color", [255, 255, 255])

        # Replace reserved words
        processed_text = replace_reserved_words(text)

        if row == -1:  # Clear all rows
            for matrix in matrices:
                matrix.fill((0, 0, 0))
                matrix.write()
            return

        render_text_on_row(processed_text, tuple(color), row)
    except Exception as e:
        print(f"Error processing message: {e}")

# MQTT Client Connection with Auto-Reconnection
def connect_to_mqtt():
    """Connect to the MQTT broker with automatic reconnection."""
    client = MQTTClient("esp32_matrix", MQTT_BROKER, port=MQTT_PORT)

    def reconnect():
        """Attempt to reconnect to the MQTT broker."""
        while True:
            try:
                print("Attempting to reconnect to MQTT broker...")
                client.connect()
                client.subscribe(MQTT_TOPIC)
                print("Reconnected to MQTT broker.")
                break
            except OSError as e:
                print(f"Reconnect failed: {e}")
                time.sleep(5)  # Retry every 5 seconds

    try:
        client.set_callback(on_message)
        client.connect()
        client.subscribe(MQTT_TOPIC)
        print(f"Connected to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}")
    except OSError as e:
        print(f"Initial connection failed: {e}")
        reconnect()

    client.reconnect = reconnect
    return client

# Main function
def main():
    connect_to_wifi()
    client = connect_to_mqtt()

    try:
        while True:
            try:
                client.check_msg()  # Check for incoming messages
                time.sleep(0.1)
            except OSError as e:
                print(f"Connection lost: {e}")
                client.reconnect()  # Attempt to reconnect
    except KeyboardInterrupt:
        print("Disconnecting...")
        client.disconnect()

# Run the main function
if __name__ == "__main__":
    main()
