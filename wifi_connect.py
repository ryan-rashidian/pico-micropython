import network # type: ignore

from time import sleep

def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)

        for _ in range(20):
            if wlan.isconnected():
                break
            sleep(0.5)

    if wlan.isconnected():
        print('Network config:', wlan.ifconfig())
        return True
    else:
        return False

