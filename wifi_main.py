from time import sleep

from wifi_connect import connect

from machine import Pin # type: ignore

led = Pin('WL_GPIO0', Pin.OUT)

SSID = 'WiFi_SSID'
PASSWORD = 'WiFi_Password'

def main():
    try:
        while True:
            print('Attempting WiFi connection...')
            connect(SSID, PASSWORD)
            print('Retrying...')
            sleep(5)
    except KeyboardInterrupt:
        led.off()
        print('Stopped by user.')

if __name__ == '__main__':
    main()
