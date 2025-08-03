from machine import Pin # type: ignore
from time import sleep

# GP0 - GP7
leds = [Pin(i, Pin.OUT) for i in range(8)]

def display_byte(byte: int):
    for i in range(8):
        # Shift each bit to LSB position and find its value.
        # Example: 
        # ASCII for 'h' = 104
        # or 01101000 in 8-bit binary
        # 104 >> 5 = 3
        # or 00000011 in 8-bit binary
        # Then compare: 3 & 1
        # or 00000011 & 00000001
        # = 00000001 = 1
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
