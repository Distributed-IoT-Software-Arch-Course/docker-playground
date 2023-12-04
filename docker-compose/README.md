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

Check the API using PostMan or a browser accessing the target API with the associated configuration file:

```bash
http://127.0.0.1:7070/api/v1/iot/inventory/location
```

You can view active containers associated to the composed application: 

```bash
docker-compose ps
```

To view the logs of all running containers at once, run the following command:

```bash
docker-compose logs
```

To view the logs of a specific target docker compose SERVICE NAME (not container name) by its name, run the following command:

```bash
docker-compose logs http-iot-inventory-api
```

To retrieve the four most recent lines of the log from all running containers, run the following command:

```bash
docker-compose logs --tail=4
```

We can continuously watch the log output in real-time by passing the -f (short for "--follow") flag to the docker-compose logs command. Run the following command to stream the logs:

```bash
docker-compose logs -f --tail=4
```

To view the logs generated until five minutes ago, run the following command:

```bash
docker-compose logs --until=5m
```

For example, to view logs that occurred between 3 P.M. and 4 P.M on May 31st, run the following command:

```bash
docker-compose logs –since=2023-05-31T15:00:00 –until=2023-05-31T16:00:00
```

You can stop the entire application with all its container using:

```bash
docker-compose down
```

You can stop, remove everything with the following command: 

```bash
docker-compose rm -fsv
```