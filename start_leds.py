#python3
#pip3
#sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
#sudo python3 -m pip install --force-reinstall adafruit-blinka
import sys
import json
import time
import board
import neopixel

PIXEL_PIN = board.D18
NUM_PIXELS = 256
NUM_ROWS = 16
NUM_COLS = 16
MATRIX=[]

ORDER = neopixel.GRB #RGB, GRB ,RGBW or GRBW.
_Pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=ORDER)

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    return tuple(int(hex[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3))

def clear_board():
    print('Clearing board.')
    for x in range(NUM_PIXELS):
        _Pixels[x] = (0,0,0)
    _Pixels.show()

def create_board(rows, cols, total_leds):
    print('Creating board.')
    slot_count = total_leds - 1
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(slot_count)
            slot_count -= 1
        if i % 2 == 1:
            row.reverse()
        MATRIX.append(row)

def draw_board(row, col, color):
    print('Lighting up LED')
    position = MATRIX[row][col]
    _Pixels[position]=color


if __name__ == '__main__':
    clear_board()
    create_board(NUM_ROWS, NUM_COLS, NUM_PIXELS)
    hex_list = json.loads(sys.argv[1])
    hex_list_length = len(hex_list)
    for i in range(hex_list_length):
        hex_list_row_length = len(hex_list[i])
        for j in range(hex_list_row_length):
            if hex_list[i][j] != '0':
                rgb = (hex_to_rgb(hex_list[i][j]))
                draw_board(i, j, rgb)
    _Pixels.show()