import json


class DeviceDescriptor:

    def __init__(self, deviceId, producer, softwareVersion):
        self.deviceId = deviceId
        self.producer = producer
        self.softwareVersion = softwareVersion

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

