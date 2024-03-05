#!/usr/bin/env python

import sys
import paho.mqtt.client as mqtt
import json

# MQTT Broker Configuration
mqtt_server_host = "172.20.10.4"
mqtt_server_port = 1883
mqtt_username = "mqtt-user"
mqtt_password = "Javier05"
mqtt_transport = "tcp"
mqtt_keepalive = 60
mqtt_client_id = "core-mosquitto"

# MQTT Topic
mqtt_topic = "home/front_door/distance"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("INFO: Connected to MQTT Broker")
    else:
        print("ERROR: Connection failed with code", rc)

def build_payload():
    payload_hash = {
        "unique_id": "ultrasonic_sensor_1",
        "name": "Ultrasonic Sensor",
        "state_topic": mqtt_topic,
        "device_class": "distance",
        "unit_of_measure": "cm",
        "distance": 10,
        "qos": 0,
        "retain": True
    }
    return json.dumps(payload_hash)

if __name__ == "__main__":
    # Connect to MQTT Broker
    client = mqtt.Client(client_id=mqtt_client_id, protocol=mqtt.MQTTv5, transport=mqtt_transport)
    client.username_pw_set(username=mqtt_username, password=mqtt_password)
    client.connect(host=mqtt_server_host, port=mqtt_server_port, keepalive=mqtt_keepalive)

    client.on_connect = on_connect
    
    # Print debug information
    print("INFO: Publishing message to MQTT topic:", mqtt_topic)
    
    # Publish Message
    payload = build_payload()
    print("INFO: Payload to be published:", payload)
    client.publish(mqtt_topic, payload)

    # Disconnect from MQTT Broker
    client.disconnect()
    sys.exit()

Traceback (most recent call last):
  File "/home/jaleman/src/client2.py", line 40, in <module>
    client = mqtt.Client(mqtt.Client, client_id=mqtt_client_id, protocol=mqtt.MQTTv5, transport=mqtt_transport)
  File "/home/jaleman/.local/lib/python3.9/site-packages/paho/mqtt/client.py", line 769, in __init__
    if self._callback_api_version not in CallbackAPIVersion:
  File "/usr/lib/python3.9/enum.py", line 373, in __contains__
    raise TypeError(
TypeError: unsupported operand type(s) for 'in': 'type' and 'EnumMeta'



