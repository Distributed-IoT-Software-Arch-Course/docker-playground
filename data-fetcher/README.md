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
