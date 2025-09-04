"""Hello World! test using 8-bit LED display."""

from machine import Pin # type: ignore
from time import sleep

# GP0 - GP7
leds = [Pin(i, Pin.OUT) for i in range(8)]

def display_byte(byte: int):
    for i in range(8):
        bit = (byte >> (7 - i)) & 1
        leds[i].value(bit)

def clear_leds():
    for led in leds:
        led.off()

def loop(text: str):
    while True:
        for char in text:
            display_byte(ord(char))
            sleep(1)
            clear_leds()
            sleep(0.25)
        sleep(3)

if __name__ == '__main__':
    try:
        print('Starting.')
        loop('Hello World.')
    except KeyboardInterrupt:
        clear_leds()
        print('Ending.')
