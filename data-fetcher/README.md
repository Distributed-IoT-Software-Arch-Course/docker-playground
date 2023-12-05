# MQTT to HTTP Inventory Integration

## Overview
This Python application demonstrates the integration between an MQTT client and an HTTP Inventory API. It uses the Paho MQTT library to connect to an MQTT broker, subscribe to a specific topic, and react to incoming messages. Upon receiving messages, the application performs HTTP requests to an API endpoint for managing IoT device inventory.

## Features

### MQTT Subscription
The application connects to an MQTT broker and subscribes to the topic "device/+/temperature". The wildcard '+' is used to dynamically capture device IDs generating temperature data.

### Message Processing
When a new MQTT message is received, the application extracts the device ID from the message topic. It then performs HTTP requests to check and create devices in the inventory.

### HTTP Requests
1. **GET Request to Check Device Existence**
   - Endpoint: `http://127.0.0.1:7070/api/iot/inventory/device/<device_id>`
   - Purpose: Checks if the device with the specified ID already exists in the inventory.

2. **POST Request to Create Device**
   - Endpoint: `http://127.0.0.1:7070/api/iot/inventory/device`
   - Payload: JSON data containing device information.
   - Purpose: If the device does not exist, creates a new device in the inventory with specified attributes.

### Device Attributes
The created devices have the following attributes:
- UUID
- Name
- Location ID
- Type
- Attributes (including min_value, unit, software_version, battery, manufacturer, max_value)

## Usage
1. Install the required libraries: `pip install paho-mqtt`.
2. Replace `"your_mqtt_broker_host"` with the actual MQTT broker hostname or IP address.
3. Run the script to connect to the MQTT broker, subscribe to the specified topic, and react to incoming messages.

Note: Make sure the HTTP Inventory API is running and accessible at `http://127.0.0.1:7070/api/iot/inventory`.

# Docker Execution

## Build the Container

```bash
docker build -t mqtt_data_fetcher:0.1 .
```

## Run the Container

Run the target container with the following configuration: 

- naming the container `mqtt_data_fetcher` using `--name=mqtt_data_fetcher`
- running it in daemon mode `-d`
- setting a restart always mode with `--restart always`

```bash
docker run --name=mqtt_data_fetcher --restart always -d mqtt_data_fetcher:0.1
```

## Run the Container using a different configuration file (e.g., changing the default API base path)

The file `test_fetcher_conf.yaml` contains a changed configuration with the correct broker IP address of the host machine and the target HTTP endpoing (in our example):

```yaml
broker_ip: "192.168.1.113"
broker_port: 1883
target_telemetry_topic: "device/+/temperature"
device_api_url: "http://192.168.1.113:7070/api/v1/iot/inventory/location/l0001/device"
```

You can pass the local file to overwrite the original on in the image container using the syntax `-v local_file_path:container_image_file_path` as follows:

```bash
docker run --name=mqtt_data_fetcher -v <PATH_TO_FILE>/test_fetcher_conf.yaml:/app/fetcher_conf.yaml --restart always -d mqtt_data_fetcher:0.1
```

On Linux System you can use the `${PWD}` command to automatically retrieve the path to the current local folder

```bash
docker run --name=mqtt_data_fetcher -v ${PWD}/test_fetcher_conf.yaml:/app/fetcher_conf.yaml --restart always -d mqtt_data_fetcher:0.1
```

## Stop & Remove the Container

```bash
docker stop mqtt_data_fetcher
docker rm mqtt_data_fetcher
```
