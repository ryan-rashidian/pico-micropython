"""WiFi test for Pico-2_W"""

from time import sleep
import network # type: ignore
from machine import Pin # type: ignore

SSID = 'SSID'
PASSWORD = 'PW'

led = Pin('WL_GPIO0', Pin.OUT)
wlan = network.WLAN(network.STA_IF)

wlan.active(True)
# Disable 'Power Saving Mode'
wlan.config(pm=wlan.PM_NONE)

def connect():
    if not wlan.isconnected():
        wlan.connect(SSID, PASSWORD)
        for _ in range(30):
            if wlan.isconnected():
                led.on()
                print(f'Connected to Wifi network: {SSID}')
                print('Network config:', wlan.ifconfig())
                break
            sleep(0.5)

def disconnect():
    wlan.disconnect()
    wlan.active(False)
    led.off()

if __name__ == '__main__':
    try:
        print('Program start.')
        connect()
    except KeyboardInterrupt:
        disconnect()
        print('Program stop.')

