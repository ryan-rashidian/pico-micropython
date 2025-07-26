from time import sleep

from wifi_connect import connect, disconnect

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
        print('Stopped by user.')
        disconnect()

if __name__ == '__main__':
    main()
