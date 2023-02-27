def serialize(obj, file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'wb') as f:
            pickle.dump(obj, f)
    elif type == 'json':
        import json
        with open(file, 'w') as f:
            json.dump(obj, f)
    else:
        print('Invalid serialization. Use pickle or json!')


# Deserializing from from to Python Object
def deserialize(file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'rb') as f:
            obj = pickle.load(f)
        return obj
    elif type == 'json':
        import json
        with open(file, 'r') as f:
            obj = json.load(f)
            return obj
    else:
        print('Invalid serialization. Use pickle or json!')


if __name__ == "__main__":
    d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}

    # Serializing using pickle
    serialize(d1, 'a.dat', 'pickle')

    # Deserializing
    myDict = deserialize('a.dat', 'pickle')
    print(f'pickle: {myDict}')

    print('#' * 20)

    # serializing using pickle
    serialize(d1, 'a.json', 'json')

    # deserializing
    x = deserialize('a.json', 'json')
    # Notice how the tuple value was not preserved!
    print(f'json: {x}')