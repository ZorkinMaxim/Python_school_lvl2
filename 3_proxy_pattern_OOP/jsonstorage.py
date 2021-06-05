import json


class JSONStorage:
    def __init__(self):
        self.name = "data.txt"

    def save(self, data):
        with open('data.txt', 'w') as f:
            json.dump(data, f)

    def load(self):
        with open('data.txt', 'r') as json_file:
            data = json.load(json_file)
        return data
