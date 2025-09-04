"""On-board LED blink test for Pico-2_W"""

from machine import Pin # type: ignore
from time import sleep

led = Pin('WL_GPIO0', Pin.OUT)

def main():
    while True:
        led.toggle()
        sleep(1)

def destroy():
    led.off()

if __name__ == '__main__':
    try:
        print('Program start.')
        main()
    except KeyboardInterrupt:
        destroy()
        print('Program stop.')

