import json
import requests
import paho.mqtt.client as mqtt
import yaml

# Default Values
CONF_FILE_PATH = "fetcher_conf.yaml"

# Default Configuration Dictionary
configuration_dict = {
    "broker_ip": "127.0.0.1",
    "broker_port": 1883,
    "target_telemetry_topic": "device/+/temperature",
    "device_api_url": "http://127.0.0.1:7070/api/v1/iot/inventory/location/l0001/device"
}

# Read Configuration from target Configuration File Path
def read_configuration_file():
    global configuration_dict

    with open(CONF_FILE_PATH, 'r') as file:
        configuration_dict = yaml.safe_load(file)

    return configuration_dict

configuration_dict = read_configuration_file()

print("Read Configuration from file ({}): {}".format(CONF_FILE_PATH, configuration_dict))

# MQTT Broker Configuration
mqtt_broker_host = configuration_dict["broker_ip"]
mqtt_broker_port = configuration_dict["broker_port"]
mqtt_topic = configuration_dict["target_telemetry_topic"]

# HTTP API Configuration
api_url = configuration_dict["device_api_url"]

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):

    if mqtt.topic_matches_sub(mqtt_topic, msg.topic):
        try:

            payload = json.loads(msg.payload.decode())
            device_id = msg.topic.split('/')[1]

            # Check if the device exists in the inventory
            check_device_url = f"{api_url}/{device_id}"
            check_device_response = requests.get(check_device_url)

            print(f'Checking Device availability {check_device_url} -> Response Code: {check_device_response.status_code}')

            if check_device_response.status_code == 404:

                print(f'New Device Detected: {device_id} Sending HTTP POST Request to: {api_url}')

                # If the device does not exist, create it
                create_device_url = api_url
                create_device_payload = {
                    "uuid": device_id,
                    "name": f"Demo Temperature Sensor {device_id}",
                    "device_type": "device.temperature",
                    "manufacturer": "ACME Inc",
                    "software_version": "0.0.1beta",
                    "latitude": 48.312321,
                    "longitude": 10.433423211
                }

                create_device_response = requests.post(create_device_url, json=create_device_payload)

                if create_device_response.status_code == 201:
                    print(f"Device {device_id} created successfully.")
                else:
                    print(f"Failed to create device {device_id}. Status code: {create_device_response.status_code}")

        except Exception as e:
            print(f"Error processing MQTT message: {str(e)}")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT Broker
client.connect(mqtt_broker_host, mqtt_broker_port, 60)

# Start the MQTT loop
client.loop_forever()
