"""Connect to WiFi."""

import config as cfg # Use a config.py for network credentials
from machine import Pin # type: ignore
import network # type: ignore
from time import sleep


wlan = network.WLAN(network.STA_IF)
led_wifi = Pin('WL_GPIO0', Pin.OUT)


def connect(ssid: str = cfg.WIFI_SSID, password: str = cfg.WIFI_PASSWORD):
    """Connect to Wifi."""
    led_wifi.off()
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

