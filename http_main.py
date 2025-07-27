import uasyncio

from http_server import connect, disconnect

SSID = 'WiFi_SSID'
PASSWORD = 'WiFi_Password'

async def main():
    await connect(SSID, PASSWORD)
    while True:
        await uasyncio.sleep(0)

if __name__ == '__main__':
    try:
        uasyncio.run(main())
    except KeyboardInterrupt:
        print('Stopped by user.')
        disconnect()
