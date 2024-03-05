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
mqtt_topic = "home/front_door/distance"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("INFO: Connected to MQTT Broker")
        # Subscribe to the topic
        client.subscribe(mqtt_topic)
    else:
        print("ERROR: Connection failed with code", rc)

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))
    print("Received message:", payload)
    # Process the received message here

if __name__ == "__main__":
    # Connect to MQTT Broker
    client = mqtt.Client(client_id=mqtt_client_id, protocol=mqtt.MQTTv5, transport=mqtt_transport)
    client.username_pw_set(username=mqtt_username, password=mqtt_password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host=mqtt_server_host, port=mqtt_server_port, keepalive=mqtt_keepalive)

    # Start the MQTT client loop
    client.loop_forever()
