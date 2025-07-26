import uasyncio

from http_server import connect, disconnect

SSID = 'WiFi_SSID'
PASSWORD = 'WiFi_Password'

async def main():
    try:
        print('Attempting WiFi connection...')
        await connect(SSID, PASSWORD)
        while True:
            await uasyncio.sleep(1)
    except KeyboardInterrupt:
        print('Stopped by user.')
        disconnect()

if __name__ == '__main__':
    uasyncio.run(main())
