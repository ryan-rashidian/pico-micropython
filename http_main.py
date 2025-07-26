import uasyncio

from http_server import connect, disconnect

SSID = 'WiFi_SSID'
PASSWORD = 'WiFi_Password'

async def main():
    await connect(SSID, PASSWORD)
    while True:
        print('Attempting WiFi connection...')
        await uasyncio.sleep(1)

if __name__ == '__main__':
    try:
        uasyncio.run(main())
    except KeyboardInterrupt:
        print('Stopped by user.')
        disconnect()
