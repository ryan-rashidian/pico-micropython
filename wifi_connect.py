from time import sleep

import network # type: ignore
from machine import Pin # type: ignore

led = Pin('WL_GPIO0', Pin.OUT)
wlan = network.WLAN(network.STA_IF)

def connect(ssid, password):
    wlan.active(True)
    # Disable 'Power Saving Mode'
    wlan.config(pm=0xa11140)
    led.on()

    if not wlan.isconnected():
        wlan.connect(ssid, password)
        print('Connecting to network...')

        for _ in range(30):
            if wlan.isconnected():
                print(f'Connected to Wifi network: {ssid}')
                break
            sleep(0.5)

    if wlan.isconnected():
        led.off()
        print('Network config:', wlan.ifconfig())
        while True:
            if not wlan.isconnected():
                print('Connection failed.')
                break

            status = wlan.status('rssi')
            print(f'RSSI: {status}')
            led.toggle()
            sleep(1)

    led.off()

def disconnect():
    wlan.disconnect()
    wlan.active(False)
    led.off()
    sleep(0.5)

