import asyncio

from http_server import connect, disconnect

SSID = 'WiFi_SSID'
PASSWORD = 'WiFi_Password'

async def main():
    await connect(SSID, PASSWORD)
    while True:
        await asyncio.sleep(0)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Stopped by user.')
        disconnect()
