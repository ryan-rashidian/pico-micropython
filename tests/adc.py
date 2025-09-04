"""Analog to Digital Conversion test for Pico-2_W"""

from machine import ADC, Pin # type: ignore
from time import sleep

adc = ADC(Pin(26))

def loop():
    while True:
        raw = adc.read_u16()
        volts = (raw / 65535) * 3.3
        print(f'Raw: {raw} | Voltage: {volts}')
        sleep(0.1)

if __name__ == '__main__':
    try:
        print('Start Program.')
        loop()
    except KeyboardInterrupt:
        print('End Program.')

