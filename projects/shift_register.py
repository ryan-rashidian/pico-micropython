"""Pico-2_W: 8-bit Shift Register.

- Using 74HC595 IC with 8 LEDs for display
- Simulated clock cycles with time.sleep()
"""
from machine import Pin # type: ignore
from time import sleep

register_clock_pin = Pin(11, Pin.OUT)
shift_clock_pin = Pin(12, Pin.OUT)
serial_pin = Pin(15, Pin.OUT)
# 74HC595 pulls LEDs to ground, and helps sink current.
# serial_pin.low() = on (1) | serial_pin.high() = off (0)
bit_on = serial_pin.low
bit_off = serial_pin.high

decimals = [d for d in range(256)]

def load_byte(dec):
    register_clock_pin.low()
    
    for i in range(8):
        shift_clock_pin.low()
        bit = (dec >> i) & 1
        if bit:
            bit_on()
        else:
            bit_off()
        sleep(0.01)
        shift_clock_pin.high()
        sleep(0.01)

    register_clock_pin.high()
    sleep(0.01)

def loop():
    while True:
        for d in decimals:
            load_byte(dec=d)
            sleep(0.22)

def destroy():
    # Shift in all zeros to turn off LEDs
    register_clock_pin.low()

    for _ in range(8):
        shift_clock_pin.low()
        bit_off()
        sleep(0.01)
        shift_clock_pin.high()
        sleep(0.01)

    register_clock_pin.high()
    sleep(0.01)

if __name__ == '__main__':
    try:
        print('Start Program.')
        loop()
    except KeyboardInterrupt:
        destroy()
        print('End Program.')

