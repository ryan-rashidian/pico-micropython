"""Connect to WiFi on a Pico-2_W"""

from machine import Pin # type: ignore
import network # type: ignore
from time import sleep


wlan = network.WLAN(network.STA_IF)
led_wifi = Pin('WL_GPIO0', Pin.OUT)


def connect(ssid: str, password: str):
    """Connect to Wifi."""
    wlan.active(True)
    wlan.config(pm=wlan.PM_NONE)

    if not wlan.isconnected():
        wlan.connect(ssid, password)
        for _ in range(30): # 15 seconds
            if wlan.isconnected():
                led_wifi.on()
                print(f'Connected to Wifi network: {ssid}')
                print('Network config:', wlan.ifconfig())
                break
            sleep(0.5)


def disconnect():
    """Disconnect from Wifi."""
    wlan.disconnect()
    wlan.active(False)
    led_wifi.off()

