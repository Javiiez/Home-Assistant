
#!/usr/bin/env python

import sys
import time
import yaml
import json
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

# Set the GPIO mode to BCM 
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the ultrasonic sensor
GPIO_TRIGGER = 18  # Pin to trigger the ultrasonic sensor
GPIO_ECHO = 24     # Pin to receive the ultrasonic sensor's echo

# Set the GPIO pins as either input or output
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Function to measure distance
def distance():
    # Send a short pulse to trigger the ultrasonic sensor
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Record the time when the ultrasonic sensor's echo is received
    StartTime = time.time()
    StopTime = time.time()

    # Wait for the echo to be received
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # Calculate the time taken for the echo
    TimeElapsed = StopTime - StartTime

    # Calculate distance based on the speed of sound (34300 cm/s)
    # Divide by 2 because the sound goes to the object and back
    distance = (TimeElapsed * 34300) / 2

    return distance

def load_mqtt_config(config_file):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("INFO :: Connected to MQTT Broker")
    else:
        print("ERROR :: Connection failed:", rc)

def build_payload(distance):
    payload_hash = {
        "unique_id": "ultrasonic_sensor_2", 
        "name": "Ultrasonic Sensor 2",
        "state_topic": "/home/front_door/distance",
        "device_class": "distance", 
        "unit_of_measure": "cm",
        "distance": distance,
        "qos": 0,
        "retain": True
    }
    return json.dumps(payload_hash)

if __name__ == "__main__":
    mqtt_config = load_mqtt_config('Home-Assistant/ha_config.yml')

    # Connect MQTT client
    client = mqtt.Client(client_id=mqtt_config['mqtt_client_id'], protocol=mqtt.MQTTv5)
    client.username_pw_set(username=mqtt_config['mqtt_username'], password=mqtt_config['mqtt_password'])
    client.connect(host=mqtt_config['mqtt_server_host'], port=mqtt_config['mqtt_server_port'],
                    keepalive=mqtt_config['mqtt_keepalive'], bind_address=mqtt_config['mqtt_bind_address'],
                    bind_port=mqtt_config['mqtt_bind_port'])

    client.on_connect = on_connect

    try:
        while True:
            # Call the distance function to measure distance
            dist = distance()

            # Publish the distance to MQTT
            client.publish("/home/front_door/distance", build_payload(dist), 0, retain=True)
            
            # Wait for 1 second before taking the next measurement
            time.sleep(1)

    except KeyboardInterrupt:
        print("INFO :: Exiting...")
        client.disconnect()
        GPIO.cleanup()
