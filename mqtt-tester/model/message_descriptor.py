import json


class MessageDescriptor:

    def __init__(self, timestamp, type, value):
        self.timestamp = timestamp
        self.type = type
        self.value = value

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
