import time
from rpi_ws281x import Adafruit_NeoPixel, Color

# Define LED strip configuration
LED_COUNT = 60        # Number of LED pixels
LED_PIN = 18          # GPIO pin connected to the pixels
LED_FREQ_HZ = 800000  # LED signal frequency in hertz
LED_DMA = 10          # DMA channel to use for generating signal
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # Set to '1' for GPIOs 13, 19, 41, 45, 53

# Create NeoPixel object
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Path to your RGB values text file
file_path = 'two.txt'  # Replace with the actual path to your file

while True:
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            try:
                # Split the line into RGB values
                r, g, b = map(int, line.strip().split(','))

                # Update the LED strip with the RGB values
                for i in range(strip.numPixels()):
                    strip.setPixelColor(i, Color(r, g, b))
                strip.show()

                print(f"Line {line_number}: RGB({r}, {g}, {b})")

            except (ValueError, IndexError):
                print(f"Error parsing RGB values on line {line_number}: {line}")

            time.sleep(0.5)  # Sleep for 1 second after processing each line