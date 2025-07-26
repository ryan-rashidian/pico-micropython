from time import sleep

import network # type: ignore
import socket
import uasyncio
from machine import Pin # type: ignore

led = Pin('WL_GPIO0', Pin.OUT)
wlan = network.WLAN(network.STA_IF)
server = socket.socket()

running = True

async def _serve_http():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    server.bind(addr)
    server.listen(1)
    print(f'HTTP server listening on: {addr}')

    global running
    while running:
        try:
            conn, addr = server.accept()
        except OSError:
            led.toggle()
            await uasyncio.sleep(1)
            continue

        led.on()
        print(f'Client connected: {addr}')
        # Read and discard HTTP request to clear socket buffer
        _ = conn.recv(1024)

        response = b"""\
        Pico 2 W running mini HTTP server.
        """
        conn.send(response)
        conn.close()
        led.off()

def _stop_server():
    global running
    running = False

async def connect(ssid, password):
    wlan.active(True)
    # Disable 'Power Saving Mode'
    wlan.config(pm=0xa11140)
    led.on()

    if not wlan.isconnected():
        wlan.connect(ssid, password)
        print('Connecting to network...')

        for _ in range(30):
            if wlan.isconnected():
                print(f'Connected to Wifi network: {ssid}')
                break
            await uasyncio.sleep(0.5)

    if wlan.isconnected():
        led.off()
        print('Network config:', wlan.ifconfig())
        uasyncio.create_task(_serve_http())

    else:
        print('Connection failed.')
        led.off()

def disconnect():
    _stop_server()
    try:
        server.close()
    except Exception:
        pass

    wlan.disconnect()
    wlan.active(False)
    led.off()
    sleep(0.5)

