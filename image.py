from PIL import Image
import time
from rpi_ws281x import *
import neopixel


# LED strip configuration:
LED_COUNT = 25        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

def set_leds_from_image_column(column):
    for i in range(image.height):
        # Get pixel color from the image
        r, g, b = image.getpixel((column, i))
        # Set the color of the corresponding LED
        strip.setPixelColor(i, Color(g, r, b))  # GRB order might be needed depending on your LED strip
    strip.show()

# Load the image
image_path = 'image.jpg'  # Specify your image path here
image = Image.open(image_path)
image = image.convert('RGB')  # Ensure image is in RGB format

# Loop through each column in the image
for column in range(image.width):
    set_leds_from_image_column(column)
    time.sleep(1)  # Pause for a second before moving to the next column, adjust as needed
