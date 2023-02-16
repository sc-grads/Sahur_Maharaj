import json

friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}
# Serializing the dictionary to a text file called `friends.json`
with open('friends.json', 'wt') as f:
    json.dump(friends, f, indent=4)
# Serializing the dictionary to a JSON encoded string
json_string = json.dumps(friends, indent=4)
print(json_string)
# Deserializing from file into a Python Object
with open('friends.json') as f:
    obj = json.load(f)
    print(type(obj))  # => dict
    print(obj)  # => friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}
# Loading a JSON encoded string intro a Python Object
json_string = """{
    "Dan": [
        20,
        "London",
        13242252
    ],
    "Maria": [
        25,
        "Madrid",
        34232424
    ]
}"""
obj = json.loads(json_string)
print(type(obj))
print(obj)