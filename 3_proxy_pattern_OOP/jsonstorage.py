import json


class JSONStorage:
    def __init__(self):
        self.name = "data.json"

    def save(self, data):
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def load(self):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
        return data
