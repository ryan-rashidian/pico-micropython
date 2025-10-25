"""Connect to MQTT broker."""

import config as cfg # Use a config.py for network credentials
from time import sleep
from umqtt.simple import MQTTClient
from wnet import wifi


mqtt_client = MQTTClient(cfg.MQTT_CLIENT_ID, cfg.MQTT_BROKER, keepalive=60)


def connect() -> None:
    """Connect to MQTT broker."""
    try:
        mqtt_client.connect()
        print("Connected to MQTT broker")
    except Exception as e:
        print(f'MQTT connection failed: {e}')


def disconnect() -> None:
    """Disconnect from MQTT broker."""
    try:
        mqtt_client.disconnect()
    except Exception:
        pass


def ping_status() -> bool:
    """Check for and re-establish connections."""
    if not wifi.wlan.isconnected():
        wifi.connect()
        return False

    try:
        mqtt_client.ping()
        return True

    except OSError:
        print('MQTT connection lost. Reconnecting...')
        try:
            mqtt_client.connect()
            print("Connected to MQTT broker")
            return True
        except Exception as e:
            print(f'MQTT reconnect failed: {e}')
            sleep(5) # Idle cooldown before reconnect
            return False

