"""Motion sensor with WiFi on/off switch."""

from machine import Pin # type: ignore
import network, socket # type: ignore
from time import sleep

SSID = 'SSID'
PASSWORD = 'PW'

wlan = network.WLAN(network.STA_IF)
led_wifi = Pin('WL_GPIO0', Pin.OUT)

sensor = Pin(15, Pin.IN)
led_sensor = Pin(16, Pin.OUT)

# Connect to WiFi
wlan.active(True)
# Disable 'Power Saving Mode'
# - increased signal strength
# - higher idle power draw 
wlan.config(pm=wlan.PM_NONE)

if not wlan.isconnected():
    wlan.connect(SSID, PASSWORD)
    # 15 seconds to establish connection
    for _ in range(30):
        if wlan.isconnected():
            led_wifi.on()
            print(f'Connected to Wifi network: {SSID}')
            print('Network config:', wlan.ifconfig())
            break
        sleep(0.5)

# Assign to port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((wlan.ifconfig()[0], 12345))

def disconnect():
    wlan.disconnect()
    wlan.active(False)
    led_wifi.off()
    sleep(0.5)

def main():
    """Program Loop."""
    sock.setblocking(False)

    power_off = True
    motion_timer = 0

    while True:
        # Idle network check
        cmd = None
        while True:
            # Drain socket buffer
            try:
                data, _ = sock.recvfrom(1024)
                cmd = data.decode().strip()
            except OSError:
                break

        if cmd == "ON":
            power_off = False
        elif cmd == "OFF":
            motion_timer = 0
            power_off = True

        # Power-on sensor logic
        if not power_off and sensor.value() == 1:
            led_sensor.on()
            motion_timer = 50
        else:
            if motion_timer > 0:
                motion_timer -= 1
            else:
                led_sensor.off()

        # Packet update frequency & motion_timer multiplier
        sleep(0.1)
 
def destroy():
    led_sensor.off()

if __name__ == '__main__':
    try:
        print('Start Program.')
        main()
    except KeyboardInterrupt:
        disconnect()
        destroy()
        print('End Program.')

