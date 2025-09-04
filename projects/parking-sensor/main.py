"""Parking Sensor/Indicator.

Description:
    Ultrasonic ranging sensor with LED indicators.

Disclaimer:
    DO NOT use your sensor for avoiding collisions in a vehicle.
"""

from time import sleep

from machine import Pin, time_pulse_us # type: ignore

# Speed of sound = 343 m/s = 0.0343 cm/µs
SPEED_S = 0.0343

pin_trigger = Pin(19, Pin.OUT)
pin_echo = Pin(16, Pin.IN)

led_red = Pin(9, Pin.OUT)
led_yellow = Pin(12, Pin.OUT)
led_green = Pin(15, Pin.OUT)

def get_distance():
    """Measure distance (cm)."""
    pin_trigger.low()
    sleep(0.001)

    # Trigger pulse
    pin_trigger.high()
    sleep(0.001)
    pin_trigger.low()

    # Take readings
    duration = time_pulse_us(pin_echo, 1, 30000)

    # Distance formula: d = vt/2
    distance_cm = (duration * SPEED_S) / 2
    return distance_cm

def main():
    """Main program loop."""
    while True:
        dist = get_distance()

        led_green.value(dist < 100)
        led_yellow.value(dist < 50)
        led_red.value(dist < 10)

        print(f'Distance: {dist:.2f} cm')
        sleep(0.1)

def destroy():
    led_green.off()
    led_yellow.off()
    led_red.off()

if __name__ == '__main__':
    try:
        print('Program Start.')
        main()
    except KeyboardInterrupt:
        destroy()
        print('Program End.')

