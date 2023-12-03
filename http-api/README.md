# Python - IoT Inventory - Demo RESTful HTTP API

This project shows a demo implementation of a simple IoT device and location inventory through 
an HTTP RESTful API.

The implementation is based on the following Python Frameworks 

- Flask: https://flask.palletsprojects.com/en/2.0.x/
- Flask RESTful: https://flask-restful.readthedocs.io/en/latest/index.html

APIs are exposed through a configurable port (7070) and accessible locally at: http://127.0.0.1:7070/api/iot/

## Modeled REST Resources

The IoT Inventory resources currently modeled are:

- Location (/location): A simple geographic location where it is possible to add on or more IoT device references
- Device (/device): A generic representation of an IoT device with basic information and customizable attributes. 
In the current implementation device's data are not handled and they are out of the scope of the demo inventory.

## Build the Container

```bash
docker build -t http_iot_inventory_api:0.1 .
```

## Run the Container

Run the target container with the following configuration: 

- exposing the port on the `7070` using `-p 7070:7070`
- naming the container `http-inventory-api` using `--name=http-inventory-api`
- running it in daemon mode `-d`
- setting a restart always mode with `--restart always`

```bash
docker run --name=http-inventory-api -p 7070:7070 --restart always -d http_iot_inventory_api:0.1
```

## Run the Container using a different configuration file (e.g., changing the default API base path)

The file `test_conf.yaml` contains a changed configuration with a new `api_prefix` and a different `port` as follows:

```yaml
rest:
  api_prefix: "/api/v1/iot/inventory"
  host: "0.0.0.0"
  port: 9090
```

You can pass the local file to overwrite the original on in the image container using the syntax `-v local_file_path:container_image_file_path` as follows:

```bash
docker run --name=http-inventory-api -p 7070:7070 -v <PATH_TO_FILE>/test_conf.yaml:/app/conf.yaml --restart always -d http_iot_inventory_api:0.1
```

On Linux System you can use the `${PWD}` command to automatically retrieve the path to the current local folder

```bash
docker run --name=http-inventory-api -p 7070:7070 -v ${PWD}/test_conf.yaml:/app/conf.yaml --restart always -d http_iot_inventory_api:0.1
```

## Stop & Remove the Container

```bash
docker stop http-inventory-api
docker rm http-inventory-api
```

