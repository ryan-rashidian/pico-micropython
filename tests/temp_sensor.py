"""Read Pico-2_W internal temperature."""

from machine import ADC # type: ignore
from time import sleep

sensor_temp = ADC(4)

def read_temp():
    reading = sensor_temp.read_u16()
    voltage = (reading / 65535) * 3.3
    # Formula from RP2350 datasheet (12.4.6 Temperature Sensor)
    temp_c = 27 - (voltage - 0.706)/0.001721
    return temp_c

def loop():
    while True:
        temp_c = read_temp()
        print(f'Internal Temperature: {temp_c:.2f} °C')
        sleep(1)

if __name__ == '__main__':
    try:
        print('Start Program.')
        loop()
    except KeyboardInterrupt:
        print('End Program.')

