"""Simulate a byte of memory with breadboard and microcontroller.

Configure with 8x LEDs as the display, and button for read_byte.
"""

from machine import Pin # type: ignore
from time import sleep

# Activated inputs when pins pull down 1 -> 0
load_button = Pin(15, Pin.IN, Pin.PULL_UP)
bits_in = [Pin(i, Pin.IN, Pin.PULL_UP) for i in range (8)]

def read_byte():
    """Read byte and print to REPL as ASCII character."""
    byte = 0
    for i in range(8):
        bit = not bits_in[i].value()
        byte = (byte << 1) | bit
    print(f'In ASCII: {chr(byte)}')

def loop():
    while True:
        if load_button.value() == 0:
            print("Loading byte...")
            read_byte()
            sleep(1)
        sleep(0.1)

if __name__ == '__main__':
    try:
        print('Starting.')
        loop()
    except KeyboardInterrupt:
        print('Ending.')
