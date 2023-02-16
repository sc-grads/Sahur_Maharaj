# Serialization  --> exchange format using pikle or json
import pickle
friends = {'dan': [20, 'london', 335], 'maria': [22, 'ukraine', 434]}
with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)

with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)
    