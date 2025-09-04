"""Pulse width modulation test."""

from machine import PWM, Pin # type: ignore
from time import sleep

pwm = PWM(Pin(15))

pwm.freq(1000)

def loop():
    while True:
        for duty in range(0, 65536, 1000):
            pwm.duty_u16(duty)
            sleep(0.01)

        for duty in range(65535, -1, -1000):
            pwm.duty_u16(duty)
            sleep(0.01)

def destroy():
    pwm.deinit()

if __name__ == '__main__':
    try:
        print('Start Program.')
        loop()
    except KeyboardInterrupt:
        destroy()
        print('End Program.')

