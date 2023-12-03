# MQTT and HTTP Inventory API Docker Compose

This Docker Compose configuration sets up two services: an MQTT broker using Eclipse Mosquitto and an HTTP Inventory API.

## Mosquitto Broker

### Configuration

- **Container Name:** my-mosquitto-broker
- **Image:** eclipse-mosquitto:2.0.12
- **Ports:** 1883:1883
- **Volumes:**
  - `${PWD}/mosquitto.conf:/mosquitto/config/mosquitto.conf`
  - `${PWD}/data:/mosquitto/data`
  - `${PWD}/log:/mosquitto/log`
- **Restart:** always

## HTTP Inventory API

### Configuration

- **Container Name:** http-inventory-api
- **Image:** http_iot_inventory_api:0.1
- **Ports:** 7070:7070
- **Volumes:** $(pwd)/test_conf.yaml:/app/conf.yaml
- **Restart:** always

### Usage

Run the application described in the compose file

```bash
docker-compose up
```

You can also run the application as a daemon in background

```bash
docker-compose up -d
```

You can stop the entire application with all its container using:

```bash
docker-compose down
```