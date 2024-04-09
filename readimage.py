#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse
from PIL import Image
import random
import cv2
import importlib

# LED strip configuration:
LED_COUNT      = 25     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 10      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Function to update LEDs based on the frame
def update_leds_from_frame(strip, frame):
    
    height, width, _ = frame.shape

    cG = random.randint(0, 255)
    cR = random.randint(0, 255)
    cB = random.randint(0, 255)
    br = random.randint(0, 255)
    strip.setBrightness( br )
    

    for i in range(LED_COUNT):
      # Map each LED to the appropriate pixel in the frame
      x, y = 0, (24 - i) % 25
      pixel_color = frame[y, x]
      #strip.setPixelColor(i, Color(pixel_color[1], pixel_color[2], pixel_color[0]))  # GRB to RGB
      #FIRST GREEN
      #SECOND RED
      #THIRD BLUE
      #GRB
      #random_int = random.randint(0, 255)
      #strip.setPixelColor(i, Color(pixel_color[2], pixel_color[1], pixel_color[2]))  # GRB to RGB
      strip.setPixelColor( i, Color( cG , cR, cB ) )
      print(pixel_color[1])
      time.sleep(1)
    strip.show()

def randomColorStripe(strip):
    cG = random.randint(0, 255)
    cR = random.randint(0, 255)
    cB = random.randint(0, 255)
    br = random.randint(0, 255)
    strip.setBrightness( br )

    for i in range(LED_COUNT):
      strip.setPixelColor( i, Color( cG , cR, cB ) )
      time.sleep(1)
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

  # Load video
  video_path = 'video.mp4'
  cap = cv2.VideoCapture(video_path)

  print ('Press Ctrl-C to quit.')
  if not args.clear:
      print('Use "-c" argument to clear LEDs on exit')

  try:

      while cap.isOpened():
        randomColorStripe()
        #ret, frame = cap.read()
        #if not ret:
            # Reset video to start
         #   cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
          #  continue
        #update_leds_from_frame(strip, frame)

  finally:
    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()