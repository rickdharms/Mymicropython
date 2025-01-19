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
WIFI_SSID = "SSID"
WIFI_PASSWORD = "PASSWORD"

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

# Per-row brightness levels (0.0 to 1.0)
row_brightness = [1.0] * len(ROW_PINS)

def apply_gamma_correction(color, brightness):
    """Apply gamma correction and brightness adjustment."""
    gamma = 2.8
    return [
        int((c / 255.0) ** gamma * 255 * brightness)
        for c in color
    ]

# Connect to WiFi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    print("Connecting to WiFi...")
    while not wlan.isconnected():
        time.sleep(1)
    print(f"Connected to WiFi, IP address: {wlan.ifconfig()[0]}")

# Map matrix coordinates to LED index for vertical serpentine layout
def map_matrix(x, y):
    col = x
    if col % 2 == 0:  # Even column
        return col * MATRIX_HEIGHT + y
    else:  # Odd column
        return col * MATRIX_HEIGHT + (MATRIX_HEIGHT - 1 - y)  # Reverse y for odd columns

# Render a character on a specific row
def render_character(character, x_offset, color, matrix, brightness):
    """Render a single character on the matrix."""
    char_data = bigfont.get(character, [0] * 8)  # Default: empty character
    adjusted_color = apply_gamma_correction(color, brightness)
    for y, row in enumerate(char_data):
        for x in range(8):
            if row & (1 << (7 - x)):  # Check each bit
                index = map_matrix(x + x_offset, y)
                if 0 <= index < len(matrix):  # Bounds check
                    matrix[index] = tuple(adjusted_color)

# Render text on a specific row
def render_text_on_row(text, color, row_index):
    """Render a line of text on a specific row."""
    matrix = matrices[row_index]
    brightness = row_brightness[row_index]
    matrix.fill((0, 0, 0))  # Clear the row
    x_offset = 0  # Start at the left
    for char in text:
        render_character(char, x_offset, color, matrix, brightness)
        x_offset += 8  # Move to the next character
        if x_offset >= MATRIX_WIDTH:  # Prevent overflow
            break
    matrix.write()

def replace_reserved_words(text):
    """Replace reserved words like #DATE and #TIME with actual values."""
    try:
        if "#DATE" in text or "#TIME" in text:
            ntp_host = "pool.ntp.org"
            ntp_port = 123
            buf = b'\x1b' + 47 * b'\0'

            addr = socket.getaddrinfo(ntp_host, ntp_port)[0][-1]
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(1)
            s.sendto(buf, addr)
            msg, _ = s.recvfrom(48)
            s.close()

            # Extract and validate the timestamp
            ntp_time = struct.unpack("!I", msg[40:44])[0]
            epoch = ntp_time - 2208988800  # Convert NTP time to Unix epoch
            print(f"NTP Time: {ntp_time}, Unix Epoch: {epoch}")

            if epoch < 0 or epoch > 2147483647:  # Ensure valid Unix timestamp
                raise ValueError("Invalid NTP timestamp received.")

            tm = time.localtime(epoch - 8 * 3600)  # Adjust for Pacific Time (UTC-8)

            formatted_date = f"{tm[2]:02d}/{tm[1]:02d}/{tm[0]}"
            formatted_time24 = f"{tm[3]:02d}:{tm[4]:02d}"
            hour12 = tm[3] % 12 or 12
            am_pm = "AM" if tm[3] < 12 else "PM"
            formatted_time12 = f"{hour12}:{tm[4]:02d} {am_pm}"

            text = text.replace("#DATE", formatted_date)
            text = text.replace("#TIME1", formatted_time24)
            text = text.replace("#TIME2", formatted_time12)
    except Exception as e:
        print(f"Error replacing reserved words: {e}")
    return text

# MQTT Callback for incoming messages
def on_message(topic, msg):
    try:
        print(f"Received message on topic {topic}: {msg}")
        command = json.loads(msg.decode())  # Parse JSON payload

        row = command.get("row", None)
        text = command.get("text", "")
        color = command.get("color", [255, 255, 255])
        brightness = command.get("brightness", None)  # New brightness parameter

        text = replace_reserved_words(text)  # Replace reserved words

        if brightness is not None and 0.0 <= brightness <= 1.0:
            if row == -1:  # Apply to all rows
                for i in range(len(row_brightness)):
                    row_brightness[i] = brightness
            elif 0 <= row < len(row_brightness):
                row_brightness[row] = brightness

        if row == -1:  # Clear all rows
            for matrix in matrices:
                matrix.fill((0, 0, 0))
                matrix.write()
            return

        render_text_on_row(text, tuple(color), row)
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
