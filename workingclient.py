#!/usr/bin/env python

# TO DO: take a look at looping the fake publish. 

import sys
import time
import yaml
import json
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup() 

with open('Home-Assistant/ha_config.yml', 'r') as file:
    mqtt_config = yaml.safe_load(file)
    


def on_connect(client, userdata, flags, rc, properties=None):
    if rc==0:
        print("INFO :: Connected to MQTT Broker")
    else:
        print("ERROR :: Connection failed:", rc)



def build_payload(distance):
    payload_hash={"unique_id": "ultrasonic_sensor_2", 
        "name": "Ultrasonic Sensor 2",
        "state_topic": "/home/front_door/distance",
        "device_class": "distance", 
        "unit_of_measure": "cm",
        "distance": distance,
        "qos": 0,
        "retain": True
    }
    payload=json.dumps(payload_hash) 
    return payload


if __name__ == "__main__":
    # connect mqttv5 client
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=mqtt_config['mqtt_client_id'], protocol=mqtt.MQTTv5, transport=mqtt_config['mqtt_transport'])
    client.username_pw_set(username=mqtt_config['mqtt_username'], password=mqtt_config['mqtt_password'])

    client.connect(host = mqtt_config['mqtt_server_host'], port = mqtt_config['mqtt_server_port'],
                    keepalive = mqtt_config['mqtt_keepalive'], bind_address = mqtt_config['mqtt_bind_address'], bind_port = mqtt_config['mqtt_bind_port'], properties = None)
    client.on_connect = on_connect
    
    dist= distance()
    
    client.publish("/home/front_door/distance", build_payload(dist), 0, retain=True)
    time.sleep(1)
        
    client.loop_stop()
    client.disconnect()
    sys.exit()
