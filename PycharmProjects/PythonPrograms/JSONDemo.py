import json
'''person = '{"name": "Bob", "languages": ["English", "Fench"]}'
print(type(person))
person_dict = json.loads(person)
print(type(person_dict))

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])
print(person_dict['name'])'''

with open('Person.json') as f:
  data = json.load(f)

print(data)