"""Pico-2_W: 8-bit Shift Register.

- Using 74HC595 IC with 8 LEDs for display
- Timer at 10Hz
"""
from machine import Pin, Timer # type: ignore

register_latch_pin = Pin(11, Pin.OUT)
shift_clock_pin = Pin(12, Pin.OUT)
serial_data_pin = Pin(15, Pin.OUT)
# 74HC595 pulls LEDs to ground, and helps sink current.
# serial_data_pin.low() = on (1) | serial_data_pin.high() = off (0)
led_on = serial_data_pin.low
led_off = serial_data_pin.high

decimals = [d for d in range(256)]
index = 0

def load_byte(dec):
    register_latch_pin.low()
    for i in range(8):
        shift_clock_pin.low()
        bit = (dec >> i) & 1
        if bit:
            led_on()
        else:
            led_off()
        shift_clock_pin.high()
    register_latch_pin.high()

def timer_callback(_):
    global index
    load_byte(decimals[index])
    index = (index + 1) % len(decimals)

def destroy():
    register_latch_pin.low()
    for _ in range(8):
        shift_clock_pin.low()
        led_off()
        shift_clock_pin.high()
    register_latch_pin.high()

if __name__ == '__main__':
    timer = Timer(-1)
    try:
        timer.init(freq=10, mode=Timer.PERIODIC, callback=timer_callback)
        print('Start Program.')
        while True:
            pass
    except KeyboardInterrupt:
        timer.deinit()
        destroy()
        print('End Program.')

