from time import sleep
import network, socket # type: ignore
from machine import Pin, PWM # type: ignore

SSID = 'SSID'
PASSWORD = 'PW'

PERIOD_MS = 20
DELAY = 0.001
CORRECTION = 0.0

MAX_PW = 2.5 + CORRECTION
MIN_PW = 0.5 - CORRECTION

led = Pin('WL_GPIO0', Pin.OUT)
wlan = network.WLAN(network.STA_IF)

servo = PWM(Pin(15))
servo.freq(50)

wlan.active(True)
# Disable 'Power Saving Mode'
wlan.config(pm=wlan.PM_NONE)

if not wlan.isconnected():
    wlan.connect(SSID, PASSWORD)
    for _ in range(30):
        if wlan.isconnected():
            led.on()
            print(f'Connected to Wifi network: {SSID}')
            print('Network config:', wlan.ifconfig())
            break
        sleep(0.5)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((wlan.ifconfig()[0], 12345))

def disconnect():
    wlan.disconnect()
    wlan.active(False)
    led.off()
    sleep(0.5)

def set_angle(angle):
    pulse = MIN_PW + (angle / 180) * (MAX_PW - MIN_PW)
    fraction = pulse / PERIOD_MS
    duty = int(fraction * 65535)
    servo.duty_u16(duty)

def loop():
    last_cmd = None

    while True:
        data, _ = sock.recvfrom(1024)
        cmd = data.decode().strip()
        if cmd == last_cmd:
            continue
        last_cmd = cmd

        if cmd == 'LEFT':
            for angle in range(0, 181, 1):
                set_angle(angle)
                sleep(DELAY)
            sleep(0.5)
        if cmd == 'RIGHT':
            for angle in range(180, -1, -1):
                set_angle(angle)
                sleep(DELAY)
            sleep(0.5)

        last_cmd = None

def destroy():
    servo.deinit()

if __name__ == '__main__':
    try:
        print('Start Program.')
        loop()
    except KeyboardInterrupt:
        disconnect()
        destroy()
        print('End Program.')

