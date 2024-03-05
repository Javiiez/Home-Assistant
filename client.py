#!/usr/bin/env python

# TO DO: take a look at looping the fake publish. 

import sys
import paho.mqtt.client as mqtt
import json


mqtt_server_host = "172.20.10.4"
mqtt_server_port = 1883
mqtt_bind_address = ""
mqtt_bind_port = 0
mqtt_username = "mqtt-user"
mqtt_password = "Javier05"
mqtt_transport = "tcp"
mqtt_keepalive = 60
mqtt_client_id = "core-mosquitto"


def on_connect(client, userdata, flags, rc, properties=None):
    if rc==0:
        print("INFO :: Connected to MQTT Broker")
    else:
        print("ERROR :: Connection failed:", rc)



def build_payload():
	payload_hash={"unique_id": "ultrasonic_sensor_1", 
		"name": "Ultrasonic Sensor",
		"state_topic": "home/front_door/distance",
		"device_class": "distance", 
		"unit_of_measure": "cm",
		"distance": 10,
		"qos": 0,
		"": True
		} retain
	payload=json.dumps(payload_hash) 
	return payload
	
		
if __name__ =
= "__main__":
    # connect mqttv5 client
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id = mqtt_client_id, protocol = mqtt.MQTTv5, transport = mqtt_transport)
    client.username_pw_set(username = mqtt_username, password = mqtt_password)
    client.connect(host = mqtt_server_host, port = mqtt_server_port,
                    keepalive = mqtt_keepalive, bind_address = mqtt_bind_address, bind_port = mqtt_bind_port, properties = None)
    client.on_connect = on_connect
    
    client.publish("home/front_door/distance", build_payload(), 0, retain=True)
    
    client.loop_stop()
    client.disconnect()
    sys.exit()
