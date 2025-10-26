"""Connect to MQTT broker."""

import config as cfg # Use a config.py for network credentials
from umqtt.simple import MQTTClient


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
    """Ping MQTT broker."""
    try:
        mqtt_client.ping()
        print('MQTT Broker connection: UP')
        return True
    except OSError:
        print('MQTT Broker connection: DOWN')
        return False

