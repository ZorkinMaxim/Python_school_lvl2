import json

new = {"siblings":4, "work":"IT park"}

with open('data.txt', 'r+') as f:
    x = json.load(f)
    x.update(new)
    f.seek(0)
    json.dump(x, f)
