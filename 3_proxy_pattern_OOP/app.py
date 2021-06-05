from storage import *

storage = StorageProxy()  # in memory
storage.save("Test Data")
print(storage.load())

storage = StorageProxy("file")  # in file
storage.save("Test Data")
print(storage.load())

storage = StorageProxy("json")  # in json
storage.save({"name": "John", "age": 30, "city": "New York"})
print(storage.load())


