from wifi_connect import connect
from machine import Pin # type: ignore
from time import sleep

led = Pin('WL_GPIO0', Pin.OUT)
led.on()

SSID = 'WiFi_SSID'
PASSWORD = 'WiFi_Password'

if connect(SSID, PASSWORD):
    print('Connection successful.')
    try:
        while True:
            led.toggle()
            sleep(1)
    except KeyboardInterrupt:
        led.off()
        print('Stopped by user.')
else:
    led.off()
    print('Connection failed.')

