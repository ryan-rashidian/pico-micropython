from machine import Pin # type: ignore
from time import sleep

sensor = Pin(15, Pin.IN)
led_indicator = Pin(16, Pin.OUT)

def main():
    while True:
        if sensor.value() == 1:
            led_indicator.on()
            sleep(5)
            led_indicator.off()
        sleep(0.1)

def destroy():
    led_indicator.off()
        
if __name__ == '__main__':
    try:
        print('Start Program.')
        main()
    except KeyboardInterrupt:
        destroy()
        print('End Program.')

