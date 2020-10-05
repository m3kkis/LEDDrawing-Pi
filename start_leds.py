#python3
#pip3
#sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
#sudo python3 -m pip install --force-reinstall adafruit-blinka
import sys
import json
import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 256
ORDER = neopixel.GRB #RGB, GRB ,RGBW or GRBW.

if __name__ == '__main__':
    my_list = json.load(sys.stdin)
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
    print my_list