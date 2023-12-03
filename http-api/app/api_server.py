from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.device_resource import DeviceResource
from resources.devices_resource import DevicesResource
from resources.locations_resource import LocationsResource
from resources.location_resource import LocationResource
from persistence.data_manager import DataManager
from model.location_model import LocationModel
from model.device_model import DeviceModel
import yaml

# Default Values
CONF_FILE_PATH = "conf.yaml"
DEFAULT_ENDPOINT_PREFIX = "/api/iot/inventory"

# Default Configuration Dictionary
configuration_dict = {
    "rest":{
        "api_prefix": DEFAULT_ENDPOINT_PREFIX, 
        "host": "0.0.0.0",
        "port": 7070
    }
}

# Read Configuration from target Configuration File Path
def read_configuration_file():
    global configuration_dict

    with open(CONF_FILE_PATH, 'r') as file:
        configuration_dict = yaml.safe_load(file)

    return configuration_dict

# Read Configuration file
configuration_dict = read_configuration_file()

print("Read Configuration from file ({}): {}".format(CONF_FILE_PATH, configuration_dict))

app = Flask(__name__)
api = Api(app)

print("Starting HTTP RESTful API Server ...")

data_manager = DataManager()

api.add_resource(LocationsResource, configuration_dict['rest']['api_prefix'] + '/location',
                 resource_class_kwargs={'data_manager': data_manager},
                 endpoint="locations",
                 methods=['GET', 'POST'])

api.add_resource(LocationResource, configuration_dict['rest']['api_prefix'] + '/location/<string:location_id>',
                 resource_class_kwargs={'data_manager': data_manager},
                 endpoint='location',
                 methods=['GET', 'PUT', 'DELETE'])

api.add_resource(DevicesResource, configuration_dict['rest']['api_prefix'] + '/location/<string:location_id>/device',
                 resource_class_kwargs={'data_manager': data_manager},
                 endpoint="devices",
                 methods=['GET', 'POST'])

api.add_resource(DeviceResource, configuration_dict['rest']['api_prefix'] + '/location/<string:location_id>/device/<string:device_id>',
                resource_class_kwargs={'data_manager': data_manager},
                 endpoint='device',
                 methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':

    # Create Demo Data

    # Demo Location
    demo_location = LocationModel("l0001",
                                  "TestBuilding",
                                  48.312321,
                                  10.433423211)

    # Add New Location
    data_manager.add_location(demo_location)

    # Demo Device for the previous location
    demo_device = DeviceModel("d0001",
                              "demo-device",
                              demo_location.uuid,
                              DeviceModel.DEVICE_TYPE_DEFAULT,
                              "ACME Inc",
                              "0.0.1beta",
                              48.312321,
                              10.433423211)

    # Add New Device
    data_manager.add_device(demo_location.uuid, demo_device)

    app.run(host=configuration_dict['rest']['host'], port=configuration_dict['rest']['port'])  # run our Flask app