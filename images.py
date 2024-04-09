from PIL import Image
import time
from rpi_ws281x import *
import argparse


# LED strip configuration:
LED_COUNT      = 25     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Load the image
image_path = 'image.jpg'  # Specify your image path here
image = Image.open(image_path)
image = image.convert('RGB')  # Ensure image is in RGB format


def set_leds_from_image_column(column):
    for i in range(image.height):
        # Get pixel color from the image
        r, g, b = image.getpixel((column, i))
        # Set the color of the corresponding LED
        strip.setPixelColor(i, Color(g, r, b))  # GRB order might be needed depending on your LED strip
    strip.show()


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        while True:
            # Loop through each column in the image
            for column in range(image.width):
              set_leds_from_image_column(column)
              time.sleep(1)  # Pause for a second before moving to the next column, adjust as needed
            

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
