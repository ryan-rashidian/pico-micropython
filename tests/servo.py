"""Servo motor test script."""

from machine import Pin, PWM # type: ignore
from time import sleep

servo = PWM(Pin(15))
servo.freq(50)

PERIOD_MS = 20
DELAY = 0.001
CORRECTION = 0.0

MAX_PW = 2.5 + CORRECTION
MIN_PW = 0.5 - CORRECTION


def set_angle(angle):
    pulse = MIN_PW + (angle / 180) * (MAX_PW - MIN_PW)
    fraction = pulse / PERIOD_MS
    duty = int(fraction * 65535)
    servo.duty_u16(duty)

def loop():
    while True:
        for angle in range(0, 181, 1):
            set_angle(angle)
            sleep(DELAY)
        sleep(0.5)
        for angle in range(180, -1, -1):
            set_angle(angle)
            sleep(DELAY)
        sleep(0.5)

def destroy():
    servo.deinit()

if __name__ == '__main__':
    try:
        print('Start Program.')
        loop()
    except KeyboardInterrupt:
        destroy()
        print('End Program.')
