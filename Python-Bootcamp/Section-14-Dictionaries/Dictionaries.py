# orderd collection of key value pairs
# keys must be immutable: Strings, ints, tuples, frozensets & unique
person = {'name': 'Shay',
          'age': 40,
          'gender': 'male',
          'age': 43}  # <-- value overriden with more than one key

print(person)
print(type(person))

d1 = dict()  # <-- empty

# Methods
print(len(person))  # <-- total kv pairs (4)
person['name'] = 'Changed'
print(person)

person['local'] = 'GMT + 2'  # <-- adds to end of dict
print(person)

person_age = person['age']  # <-- gets value of age
print(person_age)

val = person.get('a', 'Non exisiant key')  # <-- a is key name
print('val')

pers_name = person.pop('name')  # <-- removes kv pair from dict
print(pers_name, person)

print(person.popitem())  # <-- removes last ins pair as tuple

del person['age']  # <-- deletes from dict

# nested dicts
germany = {
    'cities': ['Hamburg', 'Berlin', 'Munich'],
    'info': {'population': 83_000_000, 'people': ['Einstein', 'Bach', 'Gauss']}
}
print(germany['cities'][1])  # <-- berlin
print(germany['info']['people'][-1])  # <-- Gauss

countries = [
    {'cities': ['Hamburg', 'Berlin', 'Munich'],
     'info': {'population': 83_000_000, 'people': ['Einstein', 'Bach', 'Gauss']}},

    {'cities': ['paris', 'lyon', 'bordeaux'],
     'info': {'population': 67_000_000, 'people': ['Mont', 'Marie', 'Napoleon']}}
]

print(countries[0]['cities'])
print(countries[1]['info']['people'][1])

# operations and methods
friend = person  # <-- ref same mem addr so if one changes both change
neig = person.copy()  # <-- new address
countries = {'ro': 'romaina', 'us':'america', 'de':'germain'}
countries.update({'hu':'hungry','fr':'france'})  # <--adds to end
print(countries)

# person.clear()  # <-- removes all values and keys
key = countries.keys()  # key list
key = list(key)
value = countries.values()
value = list(value)
print(countries.items())
print('name' in person)

# comprehension

names = {'tom', 'ANNE', 'Jogh', 'dAnY'}  # <-- sets comprehension
names = {n.capitalize() for n in names}
print(names)

d1 = {'a':1, 'v':2,'d':5}
d2 = {k*2:v*2 for k,v in d1.items()}
print(d1, d2)

d3 = {k.upper(): v*2 for k, v in d1.items() if v % 3 == 0}
print(d3)

years = [2017, 2018, 2019]
revnu = [30000, 40000, 50000]

z = zip(years, revnu)  # <-- pair list values
sale = list(z)
tot_sales = dict(zip(years, revnu))
profit = {k: v * 0.15 for k, v in tot_sales.items()}
print(profit)
