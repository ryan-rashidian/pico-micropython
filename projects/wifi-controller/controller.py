from time import sleep
import network, socket # type: ignore
from machine import Pin # type: ignore

SSID = 'SSID'
PASSWORD = 'PW'

led = Pin('WL_GPIO0', Pin.OUT)
wlan = network.WLAN(network.STA_IF)

button_left = Pin(11, Pin.IN, Pin.PULL_UP)
button_right = Pin(12, Pin.IN, Pin.PULL_UP)

server_ip = 'IP'
server_port = 12345

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

def disconnect():
    wlan.disconnect()
    wlan.active(False)
    led.off()
    sleep(0.5)

def loop():
    while True:
        if button_left.value() == 0:
            sock.sendto(b'LEFT', (server_ip, server_port))
            while button_left.value() == 0:
                sleep(0.01)
            sleep(0.5)
        if button_right.value() == 0:
            sock.sendto(b'RIGHT', (server_ip, server_port))
            while button_right.value() == 0:
                sleep(0.01)
            sleep(0.5)
        sleep(0.1)

if __name__ == '__main__':
    try:
        print('Start Program.')
        loop()
    except KeyboardInterrupt:
        disconnect()
        print('End Program.')

