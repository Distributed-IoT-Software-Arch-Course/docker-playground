# MQTT Temperature Sensor Example

This Python script provides an example of a simple temperature sensor using the Paho MQTT library to publish temperature data to an MQTT broker. The script utilizes the Paho MQTT library, so make sure to install it before running the script:

```bash
pip install paho-mqtt
```

## Configuration

Update the configuration variables in the script according to your setup:

### Configuration variables

```python
device_id = "test_device_1"
client_id = "clientId0001-Producer"
broker_ip = "127.0.0.1"  # Update with your MQTT broker IP
broker_port = 1883       # Update with your MQTT broker port
default_topic = "device/{}/temperature".format(device_id)
message_limit = 1000
```

## Running the Script

Run the Python script:

```bash
python your_script_name.py
```

In some deployment it might be useful to use the complete Python bin Paht. 
For example: 

```bash
/usr/local/bin/python3.9 your_script_name.py
```

## Script Overview

The script establishes a connection to an MQTT broker and continuously publishes simulated temperature data.
The TemperatureSensor class generates random temperature values.
Each message is published to the specified MQTT topic in JSON format using the MessageDescriptor class.
The script sleeps for 5 seconds between each message.
Feel free to modify the script to suit your specific use case or integrate it into a larger project.